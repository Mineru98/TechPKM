---
Language: Rust
tags:
 - Terminal-Multiplexer
 - AI-Agent
 - CLI
 - TUI
 - Rust
aliases:
 - herdr
 - 코딩 에이전트 런타임
 - 터미널 멀티플렉서
url: https://github.com/herdrdev/herdr/blob/master/README.md
---
코딩 에이전트가 실행되는 백그라운드 런타임 환경을 제공하는 터미널 멀티플렉서입니다. 세션 지속성을 통해 네트워크 끊김이나 시스템 재부팅 시에도 에이전트의 작업이 중단되지 않으며, 각 패널의 상태(작업 중, 대기, 차단)를 직관적으로 표시합니다. 단일 Rust 바이너리로 동작하며 Claude Code, Cursor 등 기존 에이전트 도구를 감싸지 않고 자체 터미널 환경에서 그대로 실행할 수 있습니다.