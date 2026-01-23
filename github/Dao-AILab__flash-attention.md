---
Language: Python
tags:
 - Attention 메커니즘
 - GPU 최적화
 - 딥러닝
 - Pytorch
 - 고성능 컴퓨팅
aliases:
 - FlashAttention
 - FlashAttention-2
 - FlashAttention-3
 - 빠른 어텐션 구현
url: https://github.com/Dao-AILab/flash-attention
---
FlashAttention은 GPU에서 메모리 효율적이고 빠른 정확한 어텐션 구현을 제공하는 프로젝트입니다. IO 인식 최적화를 통해 기존 어텐션 대비 성능을 크게 향상시키며, FlashAttention-2에서는 병렬 처리와 작업 분할을 개선하여 추가적인 속도 향상을 달성했습니다. 최신 버전의 FlashAttention-3은 Hopper GPU(예: H100)용으로 최적화되었으며 FP16/BF16/FP8 데이터 타입을 지원합니다. 이 프로젝트는 PyTorch와 호환되며, 다양한 GPU 아키텍처(NVIDIA CUDA/AMD ROCm)에서 사용 가능하며, 특히 긴 시퀀스 처리와 메모리 효율성이 중요한 대규모 언어 모델에 적합합니다.