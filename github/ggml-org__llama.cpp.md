---
Language: C/C++
tags:
 - LLM
 - Inference
 - Quantization
 - GGUF
 - LocalAI
aliases:
 - llama.cpp
 - 라마 cpp
 - libllama
url: https://github.com/ggml-org/llama.cpp/blob/master/README.md
---
외부 종속성 없는 순수 C/C++로 구현된 경량 LLM 추론 프로젝트로, 다양한 하드웨어 환경에서 최소한의 설정만으로 최고 수준의 성능을 제공하는 것을 목표로 합니다. Apple Silicon, NVIDIA, AMD GPU 등 주요 플랫폼을 최적화하여 지원하며, 다양한 비트 수준의 양자화와 CPU+GPU 하이브리드 추론을 통해 메모리 사용량을 효율적으로 줄입니다. GGUF 모델 포맷을 기반으로 CLI 도구와 OpenAI API 호환 서버를 제공하여 로컬 및 클라우드 환경에서 LLM을 손쉽게 실행하고 실험할 수 있습니다.