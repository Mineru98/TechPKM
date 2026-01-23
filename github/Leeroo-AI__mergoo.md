---
Language: Python  
tags:  
 - LLM 모델 병합  
 - Mixture-of-Experts  
 - LoRA  
 - Hugging Face  
 - 파인튜닝  
aliases:  
 - mergoo  
 - LLM 전문가 병합  
 - 모델 합병 라이브러리  
url: https://github.com/Leeroo-AI/mergoo  
---  
`mergoo`는 여러 LLM 전문가 모델을 효율적으로 병합하고 학습하는 파이썬 라이브러리입니다. Mixture-of-Experts, Mixture-of-Adapters, 레이어별 병합 방식을 지원하며, Llama, Mistral, Phi3, BERT 등 다양한 기반 모델과 호환됩니다. 병합된 모델은 Hugging Face Trainer, SFTrainer, PEFT 등을 활용해 추가 학습이 가능하며, CPU/GPU/MPS 환경에서 동작합니다.  

이 프로젝트는 여러 도메인 특화 LLM의 지식을 통합하거나 LoRA 어댑터 기반 전문가 모델을 유연하게 결합하는 데 최적화되어 있습니다. 오픈소스 라이선스로 제공되며, 지속적인 기능 확장이 진행 중인 활발한 커뮤니티가 지원합니다.