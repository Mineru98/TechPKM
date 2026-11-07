---
Language: Python
tags:
 - MCP
 - Text-to-SQL
 - SemanticLayer
 - KnowledgeBase
 - Obsidian
aliases:
 - Auto Ontology MCP
 - auto-ontology-mcp
 - 오토 온톨로지
url: https://github.com/gogoymh/auto-ontology-mcp
---
Auto Ontology MCP는 NVIDIA Auto Ontology의 시맨틱 레이어를 MCP 클라이언트(Claude Code, Codex, Cursor 등)에 연결해, 사용 중인 LLM이 데이터베이스를 모델링하고 온톨로지 기반으로 SQL을 검증·실행하며 정확한 답변을 하도록 돕는 서버다. 또한 영수증, 문서, 노트 등을 읽어 타입화된 레코드와 개념, 출처 정보로 저장하는 개인 지식 베이스 기능을 제공하며, Obsidian 볼트로 내보낼 수 있어 LLM Wiki 대안으로 사용할 수 있다. 연결된 데이터베이스는 읽기 전용으로만 접근하며, 모든 언어 처리는 클라이언트의 모델이 담당하고 서버는 로컬 SQLite에 검증·저장 등 결정론적 작업을 수행한다.