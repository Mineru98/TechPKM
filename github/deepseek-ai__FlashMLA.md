---
Language: C++
tags:
 - Attention Kernel
 - GPU 최적화
 - 딥러닝
 - PyTorch
 - CUDA
aliases:
 - FlashMLA
 - DeepSeek Attention Kernel
 - MLA 최적화
 - FlashMLA 커널
url: https://github.com/deepseek-ai/FlashMLA
---
FlashMLA는 DeepSeek-V3 및 DeepSeek-V3.2 모델을 구동하는 최적화된 어텐션 커널 라이브러리입니다. 희소 어텐션(DeepSeek Sparse Attention)과 밀집 어텐션 커널을 포함하며, MLA 연산을 가속화하여 H800 및 B200 GPU에서 높은 성능을 달성합니다. CUDA 12.8 이상과 SM90/100 아키텍처를 지원하며, FP8 KV 캐시 및 다양한 어텐션 모드를 활용한 효율적인 연산을 제공합니다.