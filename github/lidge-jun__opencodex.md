---
Language: TypeScript
tags:
 - LLM-Proxy
 - OpenAI-Codex
 - Claude-Code
 - Node.js
 - AI-Toolkit
aliases:
 - opencodex
 - OCX
 - OpenAI Codex Proxy
 - Claude Code Proxy
url: https://github.com/lidge-jun/opencodex/blob/main/README.md
---
OpenAI Codex 및 Claude Code가 지원하는 Responses API를 Anthropic, Google Gemini, Ollama 등 40개 이상의 다양한 LLM 공급자가 사용하는 API 형식으로 변환해 주는 로컬 프록시 프로젝트입니다. 사용자는 기존 Codex CLI나 앱 환경을 그대로 유지하면서 원하는 모델로 라우팅할 수 있으며, 스트리밍, 도구 호출, 토큰 처리 등 모든 기능이 양방향으로 원활하게 작동합니다. 또한 ChatGPT 계정 풀을 관리하여 세션별로 자동으로 할당량을 분산시키고 라이브 요청 로그를 제공하는 대시보드를 포함하고 있어 개발 환경의 유연성과 가시성을 크게 높여줍니다.