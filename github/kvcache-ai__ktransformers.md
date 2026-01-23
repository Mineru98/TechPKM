---
Language: Python
tags:
 - LLM 추론 최적화
 - CPU-GPU 하이브리드 컴퓨팅
 - 모델 파인튜닝
 - MoE 최적화
 - 오픈소스 프레임워크
aliases:
 - KTransformers
 - kt-kernel
 - kt-sft
 - LLM 인퍼런스
url: https://github.com/kvcache-ai/ktransformers
---
KTransformers는 CPU-GPU 이기종 컴퓨팅을 통해 대규모 언어 모델(LLM)의 효율적인 추론 및 파인튜닝을 지원하는 연구 프로젝트입니다. **kt-kernel** 모듈은 AMX/AVX 가속을 활용한 고성능 추론 커널을 제공하며, **kt-sft** 모듈은 LLaMA-Factory와 통합된 파인튜닝 프레임워크로 671B DeepSeek-V3 모델을 70GB GPU 메모리로 훈련 가능합니다. 프로젝트 목적은 최신 LLM 최적화 기술의 연구 및 적용을 위한 유연한 플랫폼 제공에 있습니다.