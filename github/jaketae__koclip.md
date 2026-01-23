---
Language: Python
tags:
 - 멀티모달 모델
 - 한국어 NLP
 - 비전-언어 모델
 - JAX/Flax
 - CLIP
aliases:
 - KoCLIP
 - 한국어 CLIP
 - 한국판 CLIP
 - koclip-base
 - koclip-large
url: https://github.com/huggingface/transformers/tree/master/examples/research_projects/jax-projects/hybrid_clip
---
KoCLIP은 OpenAI의 CLIP 모델을 한국어로 이식한 멀티모달 모델입니다. 이 프로젝트는 Hugging Face와 Google Flax/JAX 팀이 공동 주최한 커뮤니티 위크의 일환으로 진행되었으며, 한국어 이미지 캡션과 영어 번역 데이터를 활용해 학습되었습니다. 두 가지 모델 크기(`koclip-base`와 `koclip-large`)를 제공하며, 한국어와 간단한 영어 질의 모두에서 효과적인 성능을 보입니다. JAX와 PyTorch 모두에서 사용 가능하며, TPU 환경에서 최적화된 학습을 지원됩니다.