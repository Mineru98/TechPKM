---
Language: CUDA
tags:
 - CUDA 최적화
 - 행렬 곱셈 라이브러리
 - FP8/BF16 지원
 - MoE 그룹화 연산
 - JIT 컴파일
aliases:
 - DeepGEMM
 - 딥러닝 행렬 연산 최적화
 - NVIDIA GPU 커널 튜닝
url: https://github.com/deepseek-ai/DeepGEMM
---
DeepGEMM은 NVIDIA GPU에서 효율적이고 간결한 행렬 곱셈(GEMM) 연산을 위한 CUDA 기반 라이브러리입니다. FP8 및 진행 중인 BF16 데이터 형식을 지원하며, 특히 Mix-of-Experts(MoE) 모델에 최적화된 그룹화된 행렬 연산을 제공합니다. JIT(Just-In-Time) 컴파일 방식을 활용하여 설치 시 커널 컴파일 없이도 런타임에 최적화된 커널을 생성하며, CUTLASS와 CuTe의 개념을 차용하면서도 단순성과 접근성을 유지합니다. 다양한 행렬 형식에서 전문가가 튜닝한 라이브러리와 동등하거나 더 나은 성능을 달성합니다.