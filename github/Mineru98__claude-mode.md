---
Language: Shell
tags:
 - Claude-Code
 - CLI-Wrapper
 - Shell-Script
 - 개발자-도구
 - 설정-관리
aliases:
 - claude-mode
 - Claude Code 모드 래퍼
 - claude --mode
url: https://github.com/Mineru98/claude-mode
---
claude-mode는 Claude Code CLI를 감싸 `claude --mode <name>` 형태로 모드별 설정을 손쉽게 적용할 수 있게 해주는 셸 래퍼 도구입니다. `settings/settings.<name>.json`을 세션에만 `--settings` 옵션으로 전달하며 원본 설정 파일은 건드리지 않고, bash, zsh, PowerShell, CMD를 지원합니다. 백엔드, 프론트엔드, 데이터 분석, 리서치 등 14개의 사전 정의된 모드를 제공하며, JSON 모드 파일을 직접 작성해 모드를 추가할 수도 있습니다.