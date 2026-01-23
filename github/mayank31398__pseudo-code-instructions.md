---
Language: Python  
tags:  
 - 자연어처리  
 - 프롬프트엔지니어링  
 - 의사코드  
 - LLM  
 - EMNLP2023  
aliases:  
 - 의사코드프롬프트  
 - Pseudo-CodeInstructions  
 - 코드기반프롬프트  
url: https://github.com/mayankmi/Pseudo-Code-Instructions  
---
이 프로젝트는 EMNLP 2023에 발표된 논문에서 제안된 의사코드 기반 프롬프트 기법을 구현한 오픈소스 저장소입니다. Super-Natural Instructions 데이터셋의 다양한 태스크를 의사코드 형식의 명령어로 재구성하여 대형 언어 모델(LLM)의 성능을 향상시키는 것을 목표로 합니다. 코드 인스트럭션 데이터셋, 예제 생성기, 전처리 함수 템플릿을 포함하며, BLOOM/CodeGen 모델과의 호환성을 제공합니다.  

의사코드는 명확한 실행 구조와 문서화를 통해 자연어 명령의 모호성을 줄이는 데 초점을 맞추며, 분류·QA·생성 태스크에서 F1 점수 7-16%p, ROUGE-L 점수 12-38% 상대적 향상을 입증했습니다. 저장소는 Apache-2.0 라이선스 하에 제공되며, 태스크별 인스턴스 라이선스는 원본 데이터에 따릅니다.