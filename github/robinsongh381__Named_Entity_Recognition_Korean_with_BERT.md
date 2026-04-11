---
Language: Python
tags:
 - NER
 - BERT
 - KoBERT
 - CRF
 - 한국어
aliases:
 - 한국어 개체명 인식
 - KoBERT NER
 - Named Entity Recognition Korean
url: https://github.com/robinsongh381/Named_Entity_Recognition_Korean_with_BERT/blob/master/README.md
---
KoBERT 사전 학습 모델을 활용하여 한국어 개체명 인식(NER)을 수행하는 프로젝트입니다. BIO 태깅 방식을 적용하여 10가지 개체 유형을 분류하며, CRF와 LSTM-CRF를 결합한 두 가지 모델 구조를 제공합니다. 데이터 전처리, 모델 학습, 추론 과정을 스크립트로 지원하고, Komoran 품사 태거를 활용해 개체명 내 조사를 제거하는 기능도 포함하고 있습니다.