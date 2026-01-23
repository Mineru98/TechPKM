---
Language: C++
tags:
 - 음성 인식
 - 자동 음성 인식(ASR)
 - 크로스 플랫폼
 - OpenAI Whisper
 - C/C++ 구현
aliases:
 - whisper.cpp
 - Whisper C++ 구현체
 - ggml-org whisper.cpp
url: https://github.com/ggml-org/whisper.cpp
---
whisper.cpp는 OpenAI의 Whisper 자동 음성 인식(ASR) 모델을 고성능으로 C/C++로 구현한 프로젝트입니다. 순수 C/C++ 구현으로 종속성이 없으며, Apple Silicon, x86, POWER 아키텍처 등 다양한 플랫폼을 지원합니다. 혼합 정밀도, 정수 양자화, 다양한 GPU 가속 기술(NVIDIA CUDA, Vulkan, Core ML 등)을 활용하여 효율적인 추론이 가능합니다. WAV 파일을 입력으로 받아 텍스트를 출력하는 CLI 도구와 함께, iOS, Android, WebAssembly 등 다양한 환경에서의 예제를 제공합니다. 음성 활동 감지(VAD) 및 실시간 스트리밍 기능도 포함되어 있습니다.