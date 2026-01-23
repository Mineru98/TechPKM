---
Language: Python  
tags:  
 - Tree of Thoughts  
 - Large Language Model  
 - 문제 해결 알고리즘  
 - 프롬프트 엔지니어링  
 - BFS/DFS 검색  
aliases:  
 - ToT  
 - 사유트리  
 - TreeOfThoughts  
url: https://github.com/princeton-nlp/tree-of-thought-llm  
---  
이 프로젝트는 "Tree of Thoughts (ToT)" 논문의 공식 구현체로, 대형 언어 모델(LLM)을 활용한 체계적인 문제 해결 프레임워크를 제공합니다. 사고 단계를 트리 구조로 탐색하며 BFS/DFS 알고리즘을 적용해 복잡한 문제(게임24, 창의적 글쓰기 등)를 해결할 수 있습니다. Python 3.7+ 기반이며 OpenAI API와 통합되어 다양한 프롬프트 기법을 지원합니다.  

핵심 특징:  
1) 사고 단계 생성(propose/sampling), 평가(value/vote), 선택(greedy) 모듈 분리  
2) 게임24, 크로스워드, 텍스트 생성 등 다중 작업 지원  
3) 논문 실험의 재현성과 사용자 정의 작업 추가 기능 제공