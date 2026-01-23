---
Language: C/CUDA  
tags:  
 - LLM  
 - GPU 가속  
 - C/CUDA  
 - 교육 자료  
 - GPT-2/3 재현  
aliases:  
 - llm.c  
 - C로 구현한 LLM  
 - GPT-2 C 구현  
url: https://github.com/karpathy/llm.c  
---  
llm.c는 PyTorch 또는 Python 의존성 없이 순수 C/CUDA로 구현된 경량 LLM 학습 프로젝트입니다. GPT-2 및 GPT-3 모델의 재현을 목표로 하며, PyTorch 기준 구현과 비교해 약 7% 빠른 성능을 보입니다. CPU/GPU 환경에서의 학습, Flash Attention, 멀티-GPU/노드 지원 등 다양한 기능을 포함하며, 교육적 목적의 단순한 구현체도 제공합니다. MIT 라이선스로 배포되며, 다양한 언어 포팅도 활발히 이루어지고 있습니다.