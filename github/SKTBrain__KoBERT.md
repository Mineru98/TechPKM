---
Language: Python
tags:
 - 한국어 NLP
 - BERT 모델
 - 자연어 처리
 - 사전 학습 모델
 - SentencePiece
aliases:
 - KoBERT
 - 한국어 BERT
 - 한국어 트랜스포머
 - SKTBrain KoBERT
url: https://github.com/SKTBrain/KoBERT/blob/master/README.md
---
KoBERT는 한국어에 특화된 BERT 사전 학습 모델로, 기존 다국어 BERT의 한국어 성능 한계를 극복하기 위해 개발되었습니다. 한국어 위키 데이터(500만 문장, 5,400만 단어)로 학습되었으며, SentencePiece 토크나이저를 사용해 8,002개의 어휘 사전을 구축했습니다. PyTorch, ONNX, MXNet-Gluon 프레임워크에서 사용 가능하고 감성 분석, 개체명 인식, 문장 임베딩 등 다양한 한국어 NLP 태스크에 활용될 수 있습니다.