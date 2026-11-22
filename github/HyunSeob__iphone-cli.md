---
Language: Rust
tags:
 - ios-automation
 - cli
 - mcp
 - accessibility-tree
 - ai-agent
aliases:
 - iphone-cli
 - iph
 - 아이폰 CLI
url: https://github.com/HyunSeob/iphone-cli
---
iphone-cli(`iph`)는 Xcode나 WebDriverAgent 없이도 AI 에이전트가 터미널에서 실제 iPhone(iOS 27+)의 앱을 읽고 조작할 수 있게 해주는 100% Rust 기반 CLI 도구입니다. 스크린샷 대신 네이티브 접근성 트리를 읽어 구조화된 UI 요소를 제공하며, QuickJS 내장 스크립트 엔진, MCP 서버, 그리고 `done`/`not_sent`/`unknown`의 안전한 결과 계약을 통해 Claude Code나 Codex 같은 에이전트가 실기기를 안전하게 자동화할 수 있습니다. macOS와 Windows용 단일 네이티브 바이너리로 배포되어 별도의 런타임 설치 없이 USB 또는 Wi-Fi로 실제 iPhone에 연결할 수 있습니다.