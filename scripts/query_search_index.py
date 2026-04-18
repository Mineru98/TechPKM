#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

from agent_search import DEFAULT_INDEX_PATH, load_index, render_result, search_index


def main() -> int:
    parser = argparse.ArgumentParser(description="Query the local markdown search index")
    parser.add_argument("query", help="Keyword or natural language query")
    parser.add_argument("--index", default=DEFAULT_INDEX_PATH, help="Input JSON index path")
    parser.add_argument("--limit", type=int, default=5, help="Number of results to show")
    parser.add_argument("--json", action="store_true", help="Emit JSON results")
    args = parser.parse_args()

    try:
        results = search_index(load_index(Path(args.index)), args.query, args.limit)
    except FileNotFoundError as exc:
        print(str(exc))
        return 1

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    if not results:
        print("No results found.")
        return 0
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {render_result(result)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
