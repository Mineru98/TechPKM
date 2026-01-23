---
Language: Python
tags:
 - KoBERT
 - NER
 - 한국어_개체명인식
 - CRF
 - LSTM
aliases:
 - 한국어_개체명인식_모델
 - KoBERT-NER
 - BERT-LSTM-CRF
url: https://github.com/SKTBrain/KoBERT
---
이 프로젝트는 KoBERT 모델을 활용한 한국어 개체명 인식(NER) 시스템을 구현한 것으로, BIO 태깅 방식과 CRF 또는 LSTM-CRF 구조를 적용했습니다. 한국해양대학교 자연언어처리 연구실의 데이터셋(23,032개 훈련 문장)을 사용하며, 조사 제거 기능을 옵션으로 제공합니다. 실험 결과 LSTM 미사용 모델이 검증 정확도 94.1%로 더 높은 성능을 보였습니다. Python 3.6 기반으로 데이터 전처리, 모델 학습, 추론 기능을 포함합니다.