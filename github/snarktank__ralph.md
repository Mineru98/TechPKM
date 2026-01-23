---
Language: ShellScript
tags:
 - AI 개발 프레임워크
 - 자동화된 코딩 에이전트
 - 지속적 통합/테스트
aliases:
 - 랄프 프로젝트
 - Ralph AI 에이전트
 - 자동화된 PRD 구현
url: https://github.com/snarktank/ralph
---
Ralph는 AI 코딩 도구(Amp 또는 Claude Code)를 반복적으로 실행하여 PRD 요구사항이 완료될 때까지 자동화된 구현을 수행하는 프레임워크입니다. 각 반복은 독립적인 컨텍스트에서 실행되며, Git 히스토리, `progress.txt`, `prd.json`을 통해 지속성을 유지합니다. Geoffrey Huntley의 Ralph 패턴을 기반으로 설계되었으며, 작은 단위의 태스크를 점진적으로 완성해 나가는 방식으로 작동합니다. UI 작업의 경우 브라우저에서 직접 검증하는 기능도 포함되어 있습니다.  

핵심 특징:  
1. PRD 생성 → JSON 변환 → 반복적 코드 구현 파이프라인  
2. 테스트/타입 체크 통과 시 자동 커밋  
3. 컨텍스트 창 한계를 극복하기 위한 세션 분할  
4. 학습 내용을 AGENTS.md에 기록하여 재사용 가능