---
Language: Node.js
tags:
 - Claude-API
 - Proxy
 - Quota-Management
 - CLI
 - TUI
aliases:
 - TeamClaude
 - 팀클로드
 - Claude-Code-Proxy
url: https://github.com/jung-wan-kim/teamclaude/blob/master/README.md
---
Claude Code와 Anthropic API 사이에 위치하여 여러 Claude 계정의 할당량을 자동으로 관리하고 전환하는 멀티 계정 프록시 도구입니다. 사용량에 따라 우선순위를 자동 산정하여 할당량이 곧 갱신되는 계정을 우선 사용하며, 429 에러 발생 시 즉각적으로 다른 계정으로 장애 조치를 수행합니다. 대화형 TUI를 통해 실시간으로 계정 상태를 모니터링하고 수동 제어가 가능하며, 외부 의존성 없이 Node.js 내장 모듈만으로 동작합니다.