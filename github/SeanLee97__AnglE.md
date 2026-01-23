---
Language: Python  
tags:  
 - 문장 임베딩  
 - BERT  
 - LLM  
 - 유사도 계산  
 - 머신 러닝  
aliases:  
 - AnglE  
 - Angle-optimized Text Embeddings  
 - 문장 임베딩 프레임워크  
url: https://github.com/WhereIsAI/AnglE  
---  
AnglE는 논문 "AnglE: Angle-optimized Text Embeddings"에서 제안된 문장 임베딩 훈련 및 추론 프레임워크입니다. BERT/LLM 기반 모델을 활용해 최신 문장 임베딩을 구현할 수 있으며, 다양한 손실 함수(ACL24, Contrastive, CoSENT, Espresso 등)와 지원 모델(BERT, RoBERTa, LLaMA, Mistral 등)을 제공합니다. MTEB 리더보드에서 SOTA 성능을 달성한 모델 훈련을 지원하며, 단일/멀티 GPU 환경에서 유연하게 사용할 수 있습니다.  

핵심 기능으로는 추론 시 프롬프트 지원, 배치 처리 최적화, 모델 압축(레이어/임베딩 차원 축소), 다양한 데이터 포맷(유사도 점수, 검색 태스크) 호환성이 포함됩니다. Hugging Face의 공식 및 서드파티 사전 학습 모델과의 호환성을 보장합니다.