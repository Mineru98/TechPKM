---
Language: Python  
tags:  
 - LLM 최적화  
 - 컨텍스트 압축  
 - 자연어 처리  
 - NLP 태스크  
 - EMNLP 2023  
aliases:  
 - Selective Context  
 - 컨텍스트 압축 알고리즘  
 - LLM 효율성 향상  
 - Self-Information 기반 필터링  
url: https://github.com/liyucheng09/Selective_Context  
---
이 프로젝트는 대규모 언어 모델(LLM)의 컨텍스트 처리 효율성을 향상시키기 위한 "Selective Context" 기법을 제안합니다. 고정된 컨텍스트 길이 내에서 정보 밀도가 높은 문장/토큰을 선택적으로 압축함으로써, 장문 문서나 긴 대화 처리 시 LLM 성능을 유지합니다. EMNLP 2023에 채택된 논문으로, 요약/질의응답/대화 관리 등 다양한 NLP 태스크에 적용 가능하며, HuggingFace 데모를 통해 즉시 체험해볼 수 있습니다. Python 라이브러리로 제공되며, GPT-2 기반 모델과 함께 사용할 수 있습니다.