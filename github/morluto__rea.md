---
Language: TypeScript
tags:
 - 리버스엔지니어링
 - MCP
 - AI-Agent
 - 바이너리분석
 - Electron
aliases:
 - REA
 - Reverse Engineer Anything
 - rea-agents
url: https://github.com/morluto/rea
---
REA(Reverse Engineer Anything)는 AI 에이전트를 MCP 서버를 통해 네이티브 바이너리, JavaScript/Electron 앱, .NET 어셈블리, 웹사이트, 안드로이드 APK 등 다양한 대상의 리버스 엔지니어링 도구와 연결해 주는 프로젝트입니다. 소스 코드 없이도 기능의 동작 원리를 분석하고 증거와 함께 설명하며, 이를 바탕으로 유사 기능을 구현할 수 있도록 지원합니다. `npx rea-agents setup`으로 Claude Code, Cursor 등 다양한 에이전트에 등록할 수 있으며, Hopper, Ghidra, IDA 같은 네이티브 분석 엔진과 연동해 로컬에서 분석을 수행합니다.