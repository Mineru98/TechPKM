---
Language: Markdown
tags:
 - reverse-engineering
 - ai-agent
 - claude-code
 - skill
 - mcp
aliases:
 - leanrea
 - Reverse Engineer Anything
url: https://github.com/aicodeking/leanrea
---
leanrea는 REA(Reverse Engineer Anything)의 MCP 서버와 207개 도구 없이, 단 하나의 8KB SKILL.md 파일만으로 동일한 리버스 엔지니어링 작업을 수행할 수 있게 해주는 경량 스킬 프로젝트다. 에이전트에게 대상별로 가장 빠른 명령어를 라우팅해주고 재구성(recon) 명령과 주의점을 알려주어, 에이전트가 asar, otool, jadx, Ghidra 같은 기존 도구를 직접 실행하도록 한다. 벤치마크에서 REA 대비 38% 빠른 실행 시간과 35% 낮은 비용으로 동일한 정확도를 달성했다.