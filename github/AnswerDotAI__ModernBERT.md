---
Language: Python  
tags:  
 - BERT  
 - 트랜스포머  
 - 자연어처리  
 - 딥러닝  
 - HuggingFace  
aliases:  
 - ModernBERT  
 - FlexBERT  
 - 현대화된 BERT  
 - encoder-modernization  
url: https://github.com/AnswerDotAI/ModernBERT  
---
ModernBERT는 기존 BERT 아키텍처를 현대화하고 확장한 연구 프로젝트입니다. FlexBERT라는 모듈식 인코더 설계 방식을 도입하며, YAML 설정 파일로 모델을 유연하게 구성할 수 있습니다. MosaicBERT와 Flash Attention 2 기술을 기반으로 구축되었으며, 사전 훈련과 GLUE 평가, 검색 모델 훈련 등 다양한 NLP 작업에 활용 가능합니다. HuggingFace에서 모델 체크포인트를 제공하며, 효율적인 학습과 추론을 목표로 합니다.  

이 프로젝트는 Answer.AI와 LightOn의 협력으로 진행되었으며, 연구 논문의 기술적 세부사항과 블로그 포스트에서 보다 자세한 정보를 확인할 수 있습니다. 주요 특징은 메모리 효율성, 긴 컨텍스트 처리, 빠른 파인튜닝 및 추론 능력입니다.