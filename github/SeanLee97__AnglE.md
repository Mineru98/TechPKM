---
Language: Python  
tags:  
 - 문장 임베딩  
 - 머신러닝  
 - 자연어처리  
aliases:  
 - AnglE  
 - 각도 최적화 텍스트 임베딩  
url: https://github.com/SeanLee97/AnglE  
---
AnglE는 문장 임베딩 훈련을 위한 오픈소스 라이브러리로, ACL 2024에 채택된 논문 "AnglE: Angle-optimized Text Embeddings"를 구현했습니다. BERT/LLM 기반 모델을 활용해 최적의 문장 임베딩을 생성하며, Contrastive/Cosine/Espresso 손실 함수 등 다양한 훈련 방식을 지원합니다. BiLSTM 및 LoRA 기반 모델 추론이 가능하며, MTEB 리더보드에서 SOTA 성능을 달성한 모델들을 훈련시킨 프레임워크입니다. 단일/다중 GPU 훈련과 함께 HuggingFace 생태계와의 호환성을 제공합니다.