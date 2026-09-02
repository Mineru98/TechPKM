---
Language: Go
tags:
 - 파일보호
 - ai-agent
 - cli-tool
 - 보안
 - 파일시스템
aliases:
 - afl
 - agent-file-lock
 - 에이전트 파일 락
url: https://github.com/Mineru98/agent-file-lock
---
agent-file-lock(afl)은 코딩 에이전트나 사용자 권한의 프로세스가 특정 파일을 수정·삭제·이름 변경하지 못하도록 커널의 불변 플래그(chattr +i / chflags schg)로 잠그는 Go 기반 CLI 도구입니다. 부모 디렉터리에 append-only 플래그를 설정해 디렉터리 이름 변경 우회를 차단하고, PreToolUse 훅을 통해 Claude Code나 Codex 같은 에이전트에게 사람이 내린 잠금 결정이라는 이유를 일반 텍스트로 설명합니다. 런타임 의존성 없는 단일 정적 바이너리로 제공됩니다.