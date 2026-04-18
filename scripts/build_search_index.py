#!/usr/bin/env python3

import argparse
from pathlib import Path

from agent_search import DEFAULT_INDEX_PATH, DEFAULT_SOURCE_DIR, build_index, save_index


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the local markdown search index")
    parser.add_argument("--source", default=DEFAULT_SOURCE_DIR, help="Markdown root directory")
    parser.add_argument("--index", default=DEFAULT_INDEX_PATH, help="Output JSON index path")
    args = parser.parse_args()

    index_data = build_index(Path(args.source))
    save_index(Path(args.index), index_data)
    unique_files = len({doc["path"] for doc in index_data["documents"]})
    print(
        f"Indexed {index_data['document_count']} chunks from {unique_files} markdown files "
        f"into {args.index}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
