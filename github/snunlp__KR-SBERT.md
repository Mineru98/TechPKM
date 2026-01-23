---
Language: Python
tags:
 - 한국어 NLP
 - Sentence-BERT
 - 문장 임베딩
 - 유사도 계산
 - KLUE-NLI
aliases:
 - KR-SBERT
 - 한국어 SBERT
 - 문장 유사도 모델
url: https://github.com/snunlp/KR-SBERT
---
서울대학교 계산언어학 연구실에서 개발한 한국어 문장 임베딩 전용 모델입니다. KR-BERT 기반으로 사전 학습된 Sentence-BERT 모델을 KLUE-NLI 및 증강된 KorSTS 데이터셋으로 파인튜닝하여 문장 간 의미적 유사도 계산 성능을 최적화했습니다. 문장 수준 벡터 생성, 패러프레이즈 탐지, 문서 분류 등에 활용 가능하며, Python 환경에서 sentence-transformers 라이브러리를 통해 쉽게 사용할 수 있습니다.  

주요 특징으로는 in-domain 전략 기반의 데이터 증강 기법 적용과 0.8628의 높은 문서 분류 정확도(KR-SBERT-V40K-klueNLI-augSTS 버전 기준)가 있습니다.