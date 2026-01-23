---
Language: Python
tags:
 - 한국어 NLP
 - BERT 경량화
 - DistilBERT
 - 한국어 모델
 - 트랜스포머
aliases:
 - DistilKoBERT
 - 코버트 경량화
 - 한국어 DistilBERT
url: https://github.com/monologg/DistilKoBERT
---
DistilKoBERT는 SKTBrain의 KoBERT 모델을 경량화한 한국어 BERT 변형 모델입니다. 기존 12개 레이어를 3개로 축소하면서도 한국어 위키, 나무위키, 뉴스 데이터(10GB)로 재학습하여 성능을 유지하였습니다. Transformers 라이브러리와 호환되며, 토큰 타입 임베딩과 풀러 레이어를 생략한 DistilBERT 구조를 채택했습니다. NER, 감정 분석 등 한국어 다운스트림 태스크에서 기존 KoBERT 대비 1/3 크기(108MB)로 효율적인 추론이 가능합니다.