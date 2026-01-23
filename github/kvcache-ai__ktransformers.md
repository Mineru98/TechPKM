---
Language: Python  
tags:  
 - LLM 최적화  
 - CPU-GPU 하이브리드  
 - 추론 및 미세조정  
 - MoE 모델  
 - 오픈소스 프레임워크  
aliases:  
 - KTransformers  
 - kt-kernel  
 - kt-sft  
 - CPU-GPU 추론  
 - LLM 하이브리드 컴퓨팅  
url: https://github.com/kvcache-ai/ktransformers  
---  
KTransformers는 대규모 언어 모델(LLM)의 효율적인 추론 및 미세조정을 위한 CPU-GPU 이기종 컴퓨팅 프레임워크입니다. 두 가지 핵심 모듈인 [kt-kernel](https://github.com/kvcache-ai/ktransformers/tree/main/kt-kernel/) (고성능 추론 커널)과 [kt-sft](https://github.com/kvcache-ai/ktransformers/tree/main/kt-sft/) (미세조정 프레임워크)로 구성되어 있습니다. 이 프로젝트는 MoE(Mixture-of-Experts) 모델 최적화에 특화되어 있으며, AMX/AVX 가속, 양자화 지원, LoRA 통합 등의 기능을 제공합니다. 연구 및 프로덕션 환경에서의 LLM 배포를 위한 유연한 솔루션을 지향합니다.