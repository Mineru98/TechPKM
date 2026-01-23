---
Language: Python  
tags:  
 - LLM 병합  
 - Mixture-of-Experts  
 - 모델 통합  
 - HuggingFace  
 - PEFT  
aliases:  
 - mergoo  
 - LLM 전문가 병합  
 - MoE 병합  
 - Mixture-of-Adapters  
url: https://github.com/Leeroo-AI/mergoo  
---  
`mergoo`는 여러 LLM 전문가 모델을 효율적으로 병합하고 훈련하기 위한 파이썬 라이브러리입니다. Mixture-of-Experts, Mixture-of-Adapters, 레이어별 병합 방식을 지원하며, Llama, Mistral, Phi3, BERT 등의 모델과 호환됩니다. HuggingFace Trainer, SFTrainer, PEFT와 통합되어 CPU/MPS/GPU에서 병합 모델을 구성할 수 있습니다.  

주요 기능은 모델 유형별 유연한 병합, 전문가 모델 통합, 다양한 훈련 옵션(라우터만 훈련 또는 전체 미세 조정) 제공입니다. 수학, 코드, LoRA 기반 어댑터 전문가 병합 사례가 포함된 튜토리얼과 블로그가 제공됩니다. GNU LGPLv3.0 라이선스로 배포됩니다.