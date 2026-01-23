---
Language: Python
tags:
 - 모델 양자화
 - GPTQ 알고리즘
 - LLM 최적화
 - PyTorch
 - HuggingFace 통합
aliases:
 - AutoGPTQ
 - GPTQ 양자화 툴
 - LLM 경량화
url: https://github.com/AutoGPTQ/AutoGPTQ
---
AutoGPTQ는 GPTQ 알고리즘 기반의 사용자 친화적 API를 제공하는 LLM 양자화 패키지입니다. 이 프로젝트는 대형 언어 모델을 4비트 수준으로 양자화하여 메모리 사용량을 줄이면서도 추론 성능을 유지하는 것을 목표로 합니다. Hugging Face Transformers, Optimum, PEFT와의 통합 지원을 통해 양자화 모델의 학습 및 추론 접근성을 높였으며, 다양한 모델 아키텍처(Bloom, LLaMA, OPT 등)와 평가 태스크(언어 모델링, 시퀀스 분류 등)를 지원합니다. 현재 유지보수는 중단되었으며, 대안으로는 GPTQModel 프로젝트를 권장합니다.