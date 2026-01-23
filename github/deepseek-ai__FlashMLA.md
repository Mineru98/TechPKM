---
Language: C++
tags:
 - 커널 최적화
 - Attention 메커니즘
 - GPU 가속
 - PyTorch
 - 고성능 컴퓨팅
aliases:
 - FlashMLA
 - DeepSeek Sparse Attention
 - DSA
 - MLA 커널
 - FlashMLA 커널
url: https://github.com/deepseek-ai/FlashMLA
---
FlashMLA는 DeepSeek-V3 및 V3.2 모델의 고성능 Attention 연산을 위한 최적화된 커널 라이브러리입니다. 이 프로젝트는 SM90/SM100 GPU 아키텍처에서 동작하는 **Sparse Attention** 및 **Dense Attention** 커널을 제공하며, 특히 KV 캐시 최적화를 통해 640 TFLOPS(프리필) 및 410 TFLOPS(디코딩) 성능을 달성합니다. H800/B200 GPU에서 테스트된 이 커널들은 CUDA 12.8+ 및 PyTorch 2.0+ 환경에서 사용할 수 있으며, FP8 KV 캐시와 토큰 수준 희소 어텐션을 지원합니다.

### 주요 특징
- **Sparse Attention**: 디코딩 시 FP8 KV 캐시 사용, 토큰 수준 희소성으로 계산 효율성 향상
- **Dense Attention**: MHA/MQA 모드 지원, 프리필 단계에서 최대 1460 TFLOPS 성능
- **하드웨어 최적화**: NVIDIA H800/B200 및 기타 호환 GPU 아키텍처 지원
- **호환성**: 기존 인터페이스와 완전히 호환되는 성능 개선 버전 제공