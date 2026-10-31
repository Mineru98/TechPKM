---
Language: Rust
tags:
 - AI-agents
 - accessibility
 - desktop-automation
 - computer-use
 - CLI
aliases:
 - agent-desktop
 - Agent Desktop
 - 컴퓨터 유즈 에이전트
url: https://github.com/vercel-labs/agent-desktop
---
agent-desktop는 AI 에이전트가 macOS, Windows, Linux의 데스크톱 앱을 접근성 트리(accessibility tree)를 통해 읽고 조작할 수 있게 하는 CLI 및 C 라이브러리입니다. 스냅샷이 조작 가능한 요소마다 ref를 JSON으로 반환하고, 에이전트가 ref로 행동한 뒤 다시 스냅샷을 찍어 확인하는 루프를 픽셀 매칭 없이 수행합니다. 60개의 명령어, 헤드리스 동작, JSON 출력 계약, 그리고 프로세스 내 호출용 FFI 라이브러리를 제공합니다.