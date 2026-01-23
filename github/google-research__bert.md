---
Language: Python
tags:
 - BERT
 - 자연어 처리
 - 사전 학습 언어 모델
 - 트랜스포머
 - 머신러닝
aliases:
 - BERT 모델
 - BERT 프레임워크
 - BERT GitHub 프로젝트
url: https://github.com/google-research/bert
---
BERT(Bidirectional Encoder Representations from Transformers)는 다양한 자연어 처리(NLP) 작업에서 최첨단 결과를 달성하는 사전 학습 언어 모델입니다. 이 프로젝트는 Google Research에서 개발되었으며, 영어 및 다국어 버전의 사전 훈련된 모델과 TensorFlow 코드를 제공합니다. BERT는 양방향 트랜스포머 인코더를 기반으로 하며, 단어 및 문장 수준의 작업에 쉽게 적응할 수 있습니다. 소규모 모델 버전(Tiny, Mini, Small 등)과 Whole Word Masking 기법을 적용한 모델도 포함되어 있으며, 계산 리소스가 제한된 환경에서의 연구에 적합합니다. GLUE, SQuAD 등의 벤치마크에서 우수한 성능을 보이며, 다운스트림 작업에 대한 미세 조정(fine-tuning)이 용이합니다.