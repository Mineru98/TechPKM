---
Language: C++
tags:
 - CUDA
 - 고성능행렬연산
 - 딥러닝최적화
 - GEMM
 - C++템플릿
aliases:
 - CUTLASS
 - CUTLASS4.3.5
 - CUTLASSDSL
 - CuTeDSL
url: https://github.com/NVIDIA/cutlass
---
CUTLASS는 CUDA 환경에서 고성능 행렬-행렬 곱셈(GEMM) 및 관련 계산을 구현하기 위한 추상화 계층 모음입니다. Volta, Turing, Ampere, Ada, Hopper, Blackwell 아키텍처 전반에서 8b 부동소수점, 블록 스케일링 데이터 타입, FP64/FP32/TF32/FP16/BF16, 정수형 및 1비트 데이터 타입을 포함한 다양한 정밀도 연산을 지원합니다. CUTLASS 4.3.5 버전에서는 Python 기반 DSL인 CuTe DSL을 도입하여 C++ 전문 지식 없이도 고성능 커널 개발이 가능하도록 했습니다. CuTe DSL은 Ampere, Hopper, Blackwell 아키텍처의 Tensor Core를 대상으로 최적 행렬 곱셈 및 선형 대수 연산을 지원하며, JIT 컴파일, TVM-FFI 통합, L2 캐시 제어 등 향상된 기능을 제공합니다. 주요 특징으로는 Async 파이프라인, 정적 스케줄링, 프로그래밍 가능한 종속적 커널 런치(PDL) 등이 포함됩니다.