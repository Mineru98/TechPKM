---
Language: Python
tags:
 - Whisper 모델
 - JAX
 - 음성 인식
 - 고속 처리
 - TPU/GPU 지원
aliases:
 - Whisper JAX
 - Whisper Jax
 - Whisper 고속 구현
url: https://github.com/sanchit-gandhi/whisper-jax
---
이 프로젝트는 OpenAI의 Whisper 모델을 JAX로 최적화한 구현체로, 기존 PyTorch 구현 대비 **70배 이상 빠른 처리 속도**를 제공합니다. CPU/GPU/TPU에서 호환되며, 배치 처리 및 하프 정밀도 계산을 지원하여 대규모 음성 데이터를 고속으로 전사(transcribe)할 수 있습니다. Transformers 라이브러리의 Flax Whisper 구현을 기반으로 하며, Hugging Face 모델 허브와 통합되어 있습니다.  

핵심 기능으로는 데이터 병렬화(`pmap`), 타임스탬프 예측, 다중 언어 지원, PyTorch 가중치 변환 도구 등이 포함됩니다. 특히 TPU 환경에서 30분 분량의 음성을 약 30초 내에 처리하는 벤치마크를 보여주었습니다.