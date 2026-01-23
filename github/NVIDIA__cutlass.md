---
Language: C++  
tags:  
 - CUDA  
 - GEMM  
 - 고성능컴퓨팅  
 - 행렬연산  
 - 텐서코어  
aliases:  
 - CUTLASS  
 - CUDA Template Library for Advanced Subroutines and Solvers  
 - CUTLASS DSL  
url: https://github.com/NVIDIA/cutlass  
---  
CUTLASS는 CUDA 환경에서 고성능 행렬 곱셈(GEMM) 및 관련 계산을 구현하기 위한 추상화 라이브러리입니다. 계층적 분해 및 데이터 이동 전략을 통합하여 재사용 가능한 소프트웨어 컴포넌트로 구성됩니다. Volta, Turing, Ampere, Hopper, Blackwell 아키텍처를 지원하며, 다양한 데이터 타입(FP16, BF16, INT8 등)과 텐서 코어를 활용한 최적화 커널을 제공합니다. CUTLASS 4부터는 CuTe DSL이라는 Python 기반 인터페이스를 도입하여 C++ 전문성 없이도 고성능 CUDA 커널 개발이 가능하도록 했습니다. 주요 특징은 모듈성, 정책 기반 튜닝, 그리고 다양한 하드웨어 아키텍처 호환성입니다.