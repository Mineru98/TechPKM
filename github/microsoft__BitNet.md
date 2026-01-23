---
Language: C++
tags:
 - 1비트 LLM 추론
 - CPU/GPU 최적화
 - 경량화 모델
 - C++ 프레임워크
 - 마이크로소프트 연구
aliases:
 - bitnet.cpp
 - BitNet 추론 엔진
 - 1.58비트 모델 실행
url: https://github.com/microsoft/BitNet
---
bitnet.cpp는 1비트 LLM(특히 BitNet b1.58 모델)의 CPU 및 GPU에서 **고속** 및 **무손실 추론**을 위한 공식 최적화 프레임워크입니다. ARM 및 x86 CPU에서 1.37x~6.17x의 속도 향상과 55.4%~82.2%의 에너지 절감을 달성하며, 단일 CPU에서 100B 파라미터 모델 실행이 가능합니다. llama.cpp를 기반으로 하며, T-MAC의 룩업 테이블 기법을 활용한 커널을 제공합니다. Hugging Face의 다양한 1비트 모델을 지원하며, 연구 및 에지 디바이스 배포에 최적화되어 있습니다.