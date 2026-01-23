---
Language: Shell
tags:
 - TUI
 - AI Agent Management
 - tmux
 - Git Worktree
 - Terminal Tool
aliases:
 - Claude Squad
 - cs
 - AI 작업 관리
 - 멀티 세션 터미널
url: https://github.com/smtg-ai/claude-squad
---
Claude Squad는 여러 AI 에이전트(Codex, Claude, Gemini, Aider 등)를 별도의 작업 공간에서 관리하는 터미널 애플리케이션입니다. 각 작업에 독립적인 git 워크스페이스를 제공하여 충돌을 방지하며, 단일 터미널 창에서 여러 세션의 작업을 효율적으로 관리할 수 있습니다. TUI 인터페이스를 통해 세션 생성/종료, 변경 사항 검토, 코드 푸시 등의 작업을 직관적으로 수행할 수 있습니다.  

### 핵심 기능  
- 백그라운드 작업 수행 및 충돌 없는 병렬 처리  
- 세션별 독립적인 git 환경 제공  
- CLI 에이전트 통합을 위한 플러그형 아키텍처  
- 변경 사항 프리뷰 및 제어 기능 (커밋/체크아웃)  

### 주요 기술  
- **tmux** 기반 세션 격리  
- **Git Worktree**를 활용한 코드베이스 분리  
- 텍스트 기반 사용자 인터페이스(TUI) 구현  

> "여러 AI 도구를 동시에 사용하면서도 코드 충돌을 해결하고 싶다면 Claude Squad가 최적의 솔루션입니다."