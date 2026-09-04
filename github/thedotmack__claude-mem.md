---
Language: TypeScript
tags:
 - claude-code
 - memory
 - mcp
 - ai-agent
 - sqlite
aliases:
 - claude-mem
 - Grok Mem
 - CMEM
url: https://github.com/thedotmack/claude-mem
---
Claude-Mem(현재 Grok Mem으로 리브랜딩)은 Claude Code, OpenCode, Antigravity 등의 AI 코딩 에이전트를 위한 지속형 메모리 플러그인입니다. 세션 간 대화 맥락과 작업 기록을 SQLite와 Chroma 벡터 DB에 저장하고, MCP 검색 도구를 통해 자연어로 과거 프로젝트 이력을 조회하여 다음 세션에 자동으로 컨텍스트를 복원합니다. 프로그레시브 디스클로저 방식의 3단계 검색 워크플로우로 토큰 사용량을 약 10배 절감할 수 있으며, 웹 뷰어 UI와 클라우드 동기화 기능도 제공합니다.