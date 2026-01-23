---
Language: C++
tags:
 - LLM-추론-엔진
 - GPU-최적화
 - CPU/GPU-하이브리드
 - 로컬-배포
 - 모델-압축
aliases:
 - PowerInfer
 - 파워인퍼
 - LLM-고속-추론
 - 소비자-등급-GPU
 - 핫/콜드-뉴런
url: https://github.com/SJTU-IPADS/PowerInfer
---
PowerInfer는 소비자 등급 GPU/CPU에서 대규모 언어 모델(LLM) 추론을 가속화하는 오픈소스 엔진입니다. 핫/콜드 뉴런 개념을 활용한 지역성 중심 설계로 GPU 메모리 사용량을 줄이고, CPU/GPU 하이브리드 연산을 통해 Falcon-40B, Llama2 계열 등 대형 모델을 단일 GPU에서도 효율적으로 실행합니다. llama.cpp 대비 최대 11.69배 빠른 성능을 제공하며, ReLU 기반 희소 모델과 PowerInfer 전용 GGUF 포맷을 지원합니다. Windows/Linux/macOS(macOS 한정 CPU 전용)에서 작동하며, AMD GPU와 Metal 백엔드 지원을 준비 중입니다.