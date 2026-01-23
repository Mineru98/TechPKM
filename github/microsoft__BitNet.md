---
Language: C++
tags:
 - 1-bit LLM
 - CPU/GPU 추론
 - 경량화 모델
 - 양자화 기술
 - 마이크로소프트 연구
aliases:
 - bitnet.cpp
 - 1비트 언어 모델
 - BitNet 추론 프레임워크
url: https://github.com/microsoft/BitNet
---
bitnet.cpp는 1.58비트 양자화된 대형 언어 모델(LLM)의 CPU/GPU 추론 속도를 최적화한 오픈소스 프레임워크입니다. 1비트 모델의 손실 없는 고속 추론을 지원하며, ARM 및 x86 CPU에서 기존 대비 최대 6.17배 속도 향상과 82.2% 에너지 절감 효과를 달성합니다. 100B 파라미터 모델도 단일 CPU에서 인간 수준의 읽기 속도(5-7 토큰/초)로 실행 가능하며, 다양한 BitNet 및 Falcon 계열 모델을 지원합니다. Hugging Face의 공개 모델을 기반으로 한 실용적인 추론 솔루션을 제공합니다.