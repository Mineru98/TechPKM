---
Language: Python
tags:
 - Parameter-Efficient Fine-Tuning
 - HuggingFace
 - LoRA
 - AI 모델 최적화
 - Transformers
aliases:
 - PEFT
 - 파라미터 효율적 미세조정
 - PEFT 라이브러리
url: https://github.com/huggingface/peft
---
이 프로젝트는 대규모 사전 훈련 모델을 효율적으로 미세 조정하기 위한 **PEFT(Parameter-Efficient Fine-Tuning)** 방법을 제공합니다. 전체 모델 파라미터를 조정하지 않고 일부만 훈련하여 계산 및 저장 비용을 크게 줄이면서도 전체 미세 조정과 유사한 성능을 달성합니다. 주요 기술인 LoRA(Low-Rank Adaptation)를 지원하며, Transformers, Diffusers, Accelerate 등의 Hugging Face 생태계와 통합되어 있습니다. GPU 메모리 절약, 소비자 하드웨어에서의 고성능 훈련, 모델 체크포인트 크기 감소 등의 장점이 있습니다.