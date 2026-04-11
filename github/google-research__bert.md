---
Language: Python
tags:
 - NLP
 - BERT
 - Transformer
 - Pre-training
 - TensorFlow
aliases:
 - BERT
 - Bidirectional Encoder Representations from Transformers
 - 버트
url: https://github.com/google-research/bert/blob/master/README.md
---
BERT(Bidirectional Encoder Representations from Transformers)는 대규모 텍스트 코퍼스를 기반으로 사전 학습된 심층 양방향 언어 모델입니다. 문장 분류, 질의응답, NER 등 다양한 자연어 처리(NLP) 작업에서 최고 수준의 성능을 달성하며, 단일 GPU 또는 Cloud TPU에서 쉽게 파인튜닝할 수 있도록 TensorFlow 코드와 사전 학습된 체크포인트를 제공합니다. 또한 연산 자원이 제한된 환경을 위한 소형 모델(Tiny, Mini, Small, Medium 등)과 다국어 및 중국어 모델도 함께 배포하고 있습니다.