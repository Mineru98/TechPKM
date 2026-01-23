---
Language: JavaScript
tags:
 - browser-automation
 - model-context-protocol
 - LLM-integration
 - Playwright
 - accessibility-snapshot
aliases:
 - Playwright MCP 서버
 - Playwright 자동화 서버
 - LLM 웹 상호작용
url: https://github.com/microsoft/playwright/tree/v1.40.0/docs/src/server.md
---
Playwright MCP 서버는 LLM(대형 언어 모델)이 웹 페이지와 구조화된 접근성 스냅샷을 통해 상호작용할 수 있도록 하는 Model Context Protocol(MCP) 서버입니다. 시각 모델이나 스크린샷 없이도 구조화된 데이터를 기반으로 브라우징 자동화 기능을 제공하며, Playwright의 접근성 트리를 활용해 빠르고 가벼운 웹 상호작용을 가능하게 합니다. 주요 특징으로는 결정적 도구 적용, LLM 친화적 설계, 픽셀 기반 입력 방식을 배제한 접근성 기반 자동화 등이 있습니다. Node.js 18 이상에서 실행되며 VS Code, Cursor, Windsurf 등 다양한 MCP 클라이언트와 호환됩니다.