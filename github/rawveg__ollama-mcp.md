---
Language: TypeScript
tags:
 - LLM 통합
 - Ollama
 - MCP 프로토콜
 - AI 도구
 - 로컬 모델
aliases:
 - ollama-mcp
 - 모델 컨텍스트 프로토콜 서버
 - 클라우드 LLM 통합
url: https://github.com/rawveg/ollama-mcp
---
이 프로젝트는 Ollama의 로컬 LLM 모델을 MCP(Model Context Protocol) 호환 애플리케이션과 통합하는 서버를 제공합니다. Claude Desktop, Cline 등 MCP 호환 클라이언트에서 Ollama SDK의 14가지 도구를 사용할 수 있도록 지원하며, Ollama 클라우드 연동 및 웹 검색 기능도 포함됩니다. TypeScript로 작성되고 Zod 스키마 검증을 활용해 타입 안정성을 보장하며, 96% 이상의 테스트 커버리지를 갖춘 고성능 서버입니다. 로컬/클라우드 하이브리드 모드, 지능형 재시도 메커니즘, 핫스왑 아키텍처 등 확장성 있는 기능을 제공합니다.