---
Language: Python  
tags:  
 - 정보검색  
 - NLP  
 - BERT  
 - 검색모델  
 - ColBERT  
aliases:  
 - ColBERTv2  
 - ColBERT  
 - ColBERTv2 메타데이터  
 - Stanford ColBERT  
 - ColBERT 검색모델  
url: https://github.com/stanford-futuredata/ColBERT  
---  
ColBERTv2는 대규모 텍스트 컬렉션에서 밀리초 단위로 확장 가능한 BERT 기반 검색 모델입니다. 문맥적 후기 상호작용(Contextual Late Interaction)을 활용하여 토큰 수준의 세부 유사성(MaxSim)을 효율적으로 계산하며, 단일 벡터 표현 모델보다 높은 정확도를 달성합니다. MS MARCO Passage Ranking 데이터셋에서 사전 훈련된 체크포인트를 제공하며, Hugging Face Transformers와 통합되어 인덱싱 및 검색 작업을 지원합니다. 주요 활용 분야로는 정보 검색, 오픈도메인 QA, 다중 홉 추론이 있습니다.