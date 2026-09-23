---
Language: Shell
tags:
 - 이슈관리
 - AI에이전트
 - ClaudeCode
 - 워크플로우
 - 온톨로지
aliases:
 - SAMSARA
 - samsara
 - 윤회
 - 이슈 온톨로지 하네스
url: https://github.com/Mineru98/samsara
---
`samsara`는 이슈를 '인(印)'으로 다루는 이슈 온톨로지 하네스 시스템으로, Claude Code·Codex·Grok Build·ZCode 등 다양한 AI CLI에 플러그인으로 설치해 사용할 수 있습니다. 개발자는 변경 작업 전 이슈(인)를 맺고 계획·증거·검토·통합 기록을 잇는 워크플로우(`issue-create → issue-start → issue-end → issue-merge`)를 따르며, 이슈 간 의존·계층·중복 등의 관계를 경락도(온톨로지 그래프)로 관리합니다. 또한 검증·병합 분석·충돌 해소·계획 비평을 담당하는 네 가지 감시자 에이전트와 버전 각인(`issue-version`) 스킬을 통해 체계적인 이슈 순환과 릴리즈 관리를 지원합니다.