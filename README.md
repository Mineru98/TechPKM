# TechPKM

## Local Markdown Search Prototype

This repository is mostly markdown knowledge notes under `github/`. The search prototype adds a lightweight local index so another assistant or agent can search notes without a web UI or external service.

### Files

- `scripts/build_search_index.py`: scans markdown files and writes a JSON search index
- `scripts/query_search_index.py`: searches the generated index with keywords or natural language
- `scripts/agent_search.py`: shared indexing and ranking logic

### How it works

- Markdown is split into chunks by headings
- Each chunk stores `path`, `title`, `heading`, and chunk text
- Queries are tokenized and ranked with simple term overlap plus title/heading/path boosts
- The generated index is written to `.search-index/markdown-index.json`

### Usage

Build the index:

```bash
python3 scripts/build_search_index.py
```

Run a query:

```bash
python3 scripts/query_search_index.py "agent skills automation"
```

Optional flags:

```bash
python3 scripts/build_search_index.py --source github --index .search-index/markdown-index.json
python3 scripts/query_search_index.py "markdown search" --limit 10
python3 scripts/query_search_index.py "openai codex skills" --json
```

### Notes

- Uses only Python standard library modules
- Search is intended as a practical local prototype, not a semantic vector search system
- `.search-index/` is ignored by git so local rebuilds do not add noise
