---
Language: JavaScript
tags:
 - Chrome-DevTools-Protocol
 - AI-Agent
 - Browser-Automation
 - CLI
 - MCP
aliases:
 - chrome-cdp
 - Chrome CDP Skill
 - CDP CLI
url: https://github.com/pasky/chrome-cdp-skill/blob/main/README.md
---
AI 에이전트가 별도의 브라우저 인스턴스 없이 현재 실행 중인 크롬 세션을 그대로 제어하고 상호작용할 수 있도록 지원하는 CLI 도구입니다. Puppeteer 같은 중간 계층 없이 Chrome DevTools Protocol에 직접 연결하며, 탭별로 백그라운드 데몬을 유지하여 100개 이상의 탭을 안정적으로 처리합니다. 이미 로그인된 상태나 현재 작업 중인 페이지의 접근성 트리, 스크린샷, HTML 추출 및 DOM 조작 등을 에이전트에게 제공하는 것이 핵심 목적입니다.