---
Language: Python
tags:
 - Speculative Decoding
 - Block Diffusion
 - LLM Inference
 - MLX
 - vLLM
aliases:
 - DFlash
 - DFlash 2
 - Flash Speculative Decoding
url: https://github.com/z-lab/dflash/blob/main/README.md
---
DFlash는 추론 디코딩(Speculative Decoding)을 위해 설계된 경량화된 블록 디퓨전(Block Diffusion) 모델입니다. 고품질의 병렬 드래프팅을 통해 대형 언어 모델의 추론 속도를 효율적으로 향상시키며, Transformers, MLX, SGLang, vLLM 등 다양한 백엔드 환경을 지원합니다. 다양한 최신 LLM 아키텍처에 대응하는 체크포인트를 제공하여 실제 서빙 환경에서의 적용을 용이하게 합니다.