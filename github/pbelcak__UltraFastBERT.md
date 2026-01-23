---
Language: Python/C++/CUDA
tags:
 - 빠른 언어 모델링
 - BERT 최적화
 - 신경망 가속화
 - 연구 논문 구현
 - 성능 벤치마킹
aliases:
 - UltraFastBERT
 - FFF 추론 최적화
 - BERT 가속화
 - 언어 모델 속도 향상
url: https://github.com/pbelcak/UltraFastBERT
---
이 프로젝트는 "Exponentially Faster Language Modelling" 논문의 구현을 포함하며, BERT 모델의 추론 속도를 향상시키기 위한 FFF(Fast Feed Forward) 기법을 제안합니다. 논문은 arXiv(2311.10770)에 공개되어 있으며, CPU/CUDA 기반 벤치마킹과 사전 학습된 모델 가중치를 제공합니다. 주요 기능은 빠른 추론을 위한 FFF 레이어 구현, 기존 crammedBERT 확장, 다양한 하드웨어 플랫폼에서의 성능 평가입니다. HuggingFace를 통해 사전 학습 모델(UltraFastBERT-1x11-long)을 활용할 수 있으며, 연구 재현을 위한 상세한 지침을 포함합니다.