---
Language: Python  
tags:  
 - 정보검색  
 - BERT  
 - 검색엔진  
aliases:  
 - ColBERT 검색 모델  
 - ColBERT 프레임워크  
 - ColBERTv2  
url: https://github.com/stanford-futuredata/ColBERT/blob/main/README.md  
---  
ColBERT는 대규모 텍스트 컬렉션에서 빠르고 정확한 검색을 지원하는 BERT 기반 모델입니다. 토큰 단위의 임베딩 행렬 생성을 통해 세밀한 문맥 상호작용을 구현하며, MaxSim 연산자로 효율적인 유사도 계산을 수행합니다. 기존의 단일 벡터 표현 모델을 능가하는 정확도와 확장성을 제공하며, 설치, 인덱싱, 검색, 훈련 프로세스를 지원하는 포괄적인 API를 갖추고 있습니다.  

ColBERTv1과 v2 버전 모두 제공되며, Hugging Face 모델과의 호환성, GPU/CPU 지원, 분산 훈련 기능을 포함합니다. RAGatouille 라이브러리와 연동하여 애플리케이션에 쉽게 통합할 수 있습니다.