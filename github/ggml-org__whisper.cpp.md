---
Language: C++
tags:
 - 음성 인식
 - 신경망 추론
 - 오픈소스 라이브러리
 - 크로스 플랫폼
 - GPU 가속
aliases:
 - whisper.cpp
 - Whisper C++ 구현
 - ggml-org whisper.cpp
url: https://github.com/ggml-org/whisper.cpp
---
OpenAI의 Whisper 자동 음성 인식(ASR) 모델을 위한 고성능 C++ 추론 구현 프로젝트입니다. 순수 C/C++로 구현되어 종속성이 없으며, Apple Silicon, ARM NEON, AVX, Vulkan, CUDA 등의 다양한 하드웨어 최적화를 지원합니다. CPU/GPU 추론, 정수 양자화, 실시간 음성 처리, 코어 ML 및 OpenVINO 통합 등 다양한 기능을 제공하며, iOS, Android, 웹어셈블리, Docker 등 다양한 플랫폼에서 동작합니다. 경량화된 설계로 임베디드 시스템 및 오프라인 애플리케이션에 적합합니다.