---
Language: Python
tags:
 - PyTorch
 - BERT
 - CRF
 - NER
 - Korean-NLP
aliases:
 - KoBERT-CRF-NER
 - 한국어 개체명 인식
 - BERT CRF 개체명 인식기
url: https://github.com/eagle705/pytorch-bert-crf-ner
---
KoBERT와 CRF를 결합하여 한국어 개체명 인식(NER)을 수행하는 PyTorch 구현 프로젝트입니다. 사람 이름, 지명, 기관명, 날짜 등 총 10개 태그를 추출하며, 벤치마크 결과에서 CRF 추가 시 기존 KoBERT 대비 F1 스코어가 향상됨을 확인했습니다. 학습 및 추론 스크립트와 함께 모델 어텐션 시각화 기능도 제공합니다.