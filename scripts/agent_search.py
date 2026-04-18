#!/usr/bin/env python3
"""Minimal local search for markdown-heavy repositories."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_SOURCE_DIR = "github"
DEFAULT_INDEX_PATH = ".search-index/markdown-index.json"
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{1,}")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n?", re.DOTALL)
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "with",
    "you",
}


@dataclass
class SectionChunk:
    heading: str
    level: int
    text: str


def strip_front_matter(text: str) -> str:
    return FRONT_MATTER_RE.sub("", text, count=1)


def normalize_whitespace(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def tokenize(text: str) -> list[str]:
    tokens = [match.group(0).lower() for match in WORD_RE.finditer(text)]
    return [token for token in tokens if token not in STOPWORDS]


def infer_title(path: Path, text: str) -> str:
    match = HEADING_RE.search(text)
    if match:
        return match.group(2).strip()
    return path.stem.replace("__", " / ")


def split_markdown_sections(text: str) -> list[SectionChunk]:
    cleaned = strip_front_matter(text).strip()
    if not cleaned:
        return []

    matches = list(HEADING_RE.finditer(cleaned))
    if not matches:
        body = normalize_whitespace(cleaned)
        return [SectionChunk(heading="Document", level=1, text=body)] if body else []

    chunks: list[SectionChunk] = []

    preamble = normalize_whitespace(cleaned[: matches[0].start()])
    if preamble:
        chunks.append(SectionChunk(heading="Summary", level=1, text=preamble))

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(cleaned)
        heading = match.group(2).strip()
        body = normalize_whitespace(cleaned[start:end])
        if not body:
            continue
        chunks.append(
            SectionChunk(
                heading=heading,
                level=len(match.group(1)),
                text=body,
            )
        )

    return chunks


def iter_markdown_files(source_dir: Path) -> Iterable[Path]:
    for path in sorted(source_dir.rglob("*.md")):
        if path.is_file():
            yield path


def build_index(source_dir: Path) -> dict:
    source_dir = source_dir.resolve()
    documents = []
    df_counter: Counter[str] = Counter()

    for file_path in iter_markdown_files(source_dir):
        raw_text = file_path.read_text(encoding="utf-8")
        title = infer_title(file_path, raw_text)
        sections = split_markdown_sections(raw_text)

        for chunk_number, section in enumerate(sections, start=1):
            chunk_text = section.text.strip()
            if not chunk_text:
                continue

            rel_path = file_path.relative_to(source_dir.parent).as_posix()
            token_counts = Counter(tokenize(f"{title} {section.heading} {chunk_text}"))
            if not token_counts:
                continue

            df_counter.update(token_counts.keys())
            documents.append(
                {
                    "id": f"{rel_path}#{chunk_number}",
                    "path": rel_path,
                    "title": title,
                    "heading": section.heading,
                    "heading_level": section.level,
                    "chunk_number": chunk_number,
                    "text": chunk_text,
                    "token_counts": dict(token_counts),
                    "token_total": sum(token_counts.values()),
                }
            )

    total_documents = len(documents)
    return {
        "version": 1,
        "source_dir": source_dir.name,
        "document_count": total_documents,
        "idf": {
            token: round(math.log((1 + total_documents) / (1 + df)) + 1, 6)
            for token, df in sorted(df_counter.items())
        },
        "documents": documents,
    }


def score_document(query_tokens: list[str], document: dict, idf: dict[str, float]) -> tuple[float, list[str]]:
    token_counts = document["token_counts"]
    matched_tokens = [token for token in query_tokens if token in token_counts]
    if not matched_tokens:
        return 0.0, []

    title_tokens = set(tokenize(document["title"]))
    heading_tokens = set(tokenize(document["heading"]))
    path_tokens = set(tokenize(document["path"].replace("/", " ")))

    score = 0.0
    unique_matches = []
    seen = set()

    for token in matched_tokens:
        tf = token_counts[token] / max(document["token_total"], 1)
        token_score = tf * idf.get(token, 1.0) * 10
        if token in title_tokens:
            token_score += 2.5
        if token in heading_tokens:
            token_score += 1.5
        if token in path_tokens:
            token_score += 1.0
        score += token_score
        if token not in seen:
            unique_matches.append(token)
            seen.add(token)

    score += min(len(unique_matches), 5) * 0.4
    return score, unique_matches


def search_index(index_data: dict, query: str, limit: int) -> list[dict]:
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    idf = index_data.get("idf", {})
    scored_results = []

    for document in index_data.get("documents", []):
        score, matched_tokens = score_document(query_tokens, document, idf)
        if score <= 0:
            continue
        scored_results.append(
            {
                **document,
                "score": round(score, 4),
                "matched_tokens": matched_tokens,
            }
        )

    scored_results.sort(
        key=lambda item: (
            -item["score"],
            item["path"],
            item["chunk_number"],
        )
    )
    return scored_results[:limit]


def load_index(index_path: Path) -> dict:
    if not index_path.exists():
        raise FileNotFoundError(
            f"Search index not found at {index_path}. Run the indexer first."
        )
    return json.loads(index_path.read_text(encoding="utf-8"))


def save_index(index_path: Path, index_data: dict) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(index_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def render_result(result: dict) -> str:
    preview = result["text"].replace("\n", " ")
    if len(preview) > 220:
        preview = preview[:217].rstrip() + "..."
    matched = ", ".join(result["matched_tokens"])
    return (
        f"[score={result['score']}] {result['title']} :: {result['heading']}\n"
        f"  path: {result['path']}\n"
        f"  matched: {matched}\n"
        f"  preview: {preview}"
    )


def build_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local markdown search prototype")
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Build a markdown search index")
    index_parser.add_argument("--source", default=DEFAULT_SOURCE_DIR, help="Markdown root directory")
    index_parser.add_argument("--index", default=DEFAULT_INDEX_PATH, help="Output JSON index path")

    query_parser = subparsers.add_parser("query", help="Search an existing markdown index")
    query_parser.add_argument("query", help="Keyword or natural language query")
    query_parser.add_argument("--index", default=DEFAULT_INDEX_PATH, help="Input JSON index path")
    query_parser.add_argument("--limit", type=int, default=5, help="Number of results to show")
    query_parser.add_argument("--json", action="store_true", help="Emit JSON results")

    return parser


def main() -> int:
    parser = build_cli_parser()
    args = parser.parse_args()

    if args.command == "index":
        source_dir = Path(args.source)
        index_path = Path(args.index)
        index_data = build_index(source_dir)
        save_index(index_path, index_data)
        unique_files = len({doc["path"] for doc in index_data["documents"]})
        print(
            f"Indexed {index_data['document_count']} chunks from {unique_files} markdown files "
            f"into {index_path}"
        )
        return 0

    if args.command == "query":
        index_path = Path(args.index)
        index_data = load_index(index_path)
        results = search_index(index_data, args.query, args.limit)
        if args.json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
            return 0
        if not results:
            print("No results found.")
            return 0
        for idx, result in enumerate(results, start=1):
            print(f"{idx}. {render_result(result)}")
        return 0

    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
