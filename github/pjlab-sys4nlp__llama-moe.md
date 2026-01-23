---
Language: Python
tags:
 - Mixture-of-Experts
 - LLaMA
 - Continual Pre-training
 - NLP
 - 오픈소스 모델
aliases:
 - LLaMA-MoE
 - MoE 모델
 - 슬림 MoE
 - 지속적 사전학습
url: https://github.com/pjlab-sys4nlp/llama-moe
---
LLaMA-MoE는 LLaMA 모델을 기반으로 한 오픈소스 Mixture-of-Experts(MoE) 모델 시리즈로, 지속적 사전학습을 통해 구현되었습니다. 3.0~3.5B 활성화된 파라미터 규모로 배포 및 연구용으로 최적화되었으며, 다양한 전문가 구성 방법과 게이팅 전략을 지원합니다. HuggingFace에서 모델 가중치를 제공하며, NLP 평가 벤치마크에서 경쟁력 있는 성능을 입증했습니다. 주요 특징으로는 경량화 설계, 다중 전문가 구성 방법(뉴런 독립/공유), 동적 가중치 샘플링, 고성능 훈련 지원(FlashAttention-v2) 등이 포함됩니다.