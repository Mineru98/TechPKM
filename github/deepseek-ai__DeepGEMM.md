---
Language: CUDA
tags:
 - FP8
 - GEMM
 - GPU 최적화
 - MoE
 - 딥러닝
aliases:
 - DeepGEMM
 - 딥지이엠
 - NVIDIA GPU 커널 최적화
url: https://github.com/deepseek-ai/DeepGEMM
---
DeepGEMM은 NVIDIA GPU에서 FP8 및 BF16을 지원하는 고성능 행렬 곱셈(GEMM) 라이브러리입니다. CUTLASS와 CuTe의 개념을 차용하면서도 간결한 설계를 지향하며, Just-In-Time(JIT) 컴파일을 통해 설치 시 커널 컴파일이 필요 없습니다. 일반적인 밀집 행렬 곱셈과 Mix-of-Experts(MoE) 그룹화 시나리오를 모두 지원하며, 다양한 행렬 형태에서 전문가 수준의 성능을 제공합니다. 특히 SM90/SM100 아키텍처를 최적화했으며, 학습 및 추론 단계별 다양한 그룹화 기법(연속/마스크)을 지원합니다.  

**핵심 특징**:  
- NVRTC 기반 고속 커널 컴파일  
- MoE 모델 전용 그룹화 GEMM 지원 (M/K축)  
- FP8 가중치 그래디언트 계산 커널  
- DeepSeek V3.2용 가중치 ReLU MQA 로짓 계산 커널  
- CUDA PDL 및 분할/스트림 최적화 로드맵 포함  

**기술 스택**: CUDA, C++20, PyTorch, CUTLASS 4.0+  

**사용 사례**: 대규모 언어 모델(LLM) 추론/학습, MoE 아키텍처 최적화, FP8/BF16 가속 컴퓨팅.