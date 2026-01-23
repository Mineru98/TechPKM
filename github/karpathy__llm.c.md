---
Language: C/CUDA
tags:
 - LLM 훈련
 - 경량화 구현
 - GPT-2 재현
 - CUDA 최적화
 - C 언어
aliases:
 - llm.c
 - C로 구현한 LLM
 - Karpathy LLM
 - 경량 GPT-2
 - C 기반 LLM 훈련
url: https://github.com/karpathy/llm.c
---
이 프로젝트는 PyTorch나 Python 없이도 순수 C/CUDA로 LLM(대형 언어 모델)을 훈련시키는 것을 목표로 합니다. 특히 GPT-2 및 GPT-3 미니시리즈의 재현에 초점을 맞추며, PyTorch 레퍼런스 구현과 비교해 약 7% 더 빠른 성능을 보입니다. CPU 전용 fp32 구현부터 GPU 기반 최적화된 훈련 코드까지 다양한 환경에서 작동하는 간결한 C 코드를 제공합니다. 교육용으로 설계된 레이어 구현 튜토리얼과 Flash Attention 같은 최신 기술도 포함되어 있습니다. MIT 라이선스로 배포됩니다.