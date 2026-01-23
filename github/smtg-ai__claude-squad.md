---
Language: Go
tags:
 - 터미널 관리 도구
 - AI 에이전트
 - 멀티태스킹
 - TUI 인터페이스
 - Git 통합
aliases:
 - Claude Squad
 - 멀티 에이전트 관리
 - cs
url: https://github.com/smtg-ai/claude-squad
---
Claude Squad는 Claude Code, Codex, Gemini, Aider 등의 다양한 AI 에이전트를 별도의 작업 공간에서 병렬로 관리할 수 있는 터미널 애플리케이션입니다. 각 작업에 독립적인 git 작업 트리를 제공하여 충돌을 방지하고, 변경 사항을 검토하거나 커밋/푸시할 수 있는 편리한 TUI 인터페이스를 제공합니다. tmux 기반의 세션 관리와 자동화된 작업 처리(yolo/auto-accept 모드)를 지원하는 것이 핵심 특징입니다.