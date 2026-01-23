---
Language: Shell Script
tags:
 - AI 에이전시
 - 자동화 개발
 - 코드 생성
 - PRD 관리
 - 지속적 통합
aliases:
 - 랄프 AI 에이전트
 - Ralph 프로젝트
 - AI 코딩 자동화
url: https://github.com/snarktank/ralph
---
Ralph는 AI 코딩 도구(Amp 또는 Claude Code)를 반복적으로 실행하여 PRD 항목을 완료할 때까지 자동화된 개발 루프를 제공하는 프로젝트입니다. 각 반복은 독립적인 컨텍스트에서 실행되며, 진행 상황은 git 히스토리, `progress.txt`, `prd.json`을 통해 유지됩니다. Geoffrey Huntley의 랄프 패턴을 기반으로 하며, PRD 생성부터 코드 구현, 품질 검증, 커밋까지의 전체 워크플로우를 자동화합니다.  

핵심 기능으로는 PRD 생성, JSON 변환, 반복 실행, 피드백 루프, 브라우저 검증, 디버깅 도구 등이 포함됩니다. 대규모 작업을 작은 단위로 분할하여 컨텍스트 한계 내에서 처리하며, 학습 내용을 `AGENTS.md`에 기록하여 향후 작업에 활용합니다. Amp 또는 Claude Code 도구와 호환되며, 프로젝트 요구사항에 맞춰 프롬프트 및 품질 검증 로직을 커스터마이징할 수 있습니다.