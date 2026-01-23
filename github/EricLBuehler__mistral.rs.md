---
Language: Rust
tags:
 - LLM 추론 엔진
 - 멀티모달
 - 크로스플랫폼
aliases:
 - mistral.rs
 - LLM 추론
 - 멀티모델 추론
url: https://github.com/EricLBuehler/mistral.rs
---
mistral.rs는 텍스트, 비전, 음성, 이미지 생성, 임베딩을 지원하는 크로스플랫폼 초고속 LLM 추론 엔진입니다. Rust와 Python API를 제공하며, OpenAI 호환 HTTP 서버, MCP 클라이언트, 다양한 양자화 및 최적화 기술(ISQ, FlashAttention, PagedAttention)을 활용하여 높은 성능을 구현합니다. Hugging Face 모델, GGUF/GGML 포맷, 다양한 아키텍처(Mistral, Llama, Gemma, Qwen 등)를 지원하며, 멀티-GPU 및 CPU 가속화를 통한 유연한 배포가 가능합니다. 웹 채팅 앱과 대화형 터미널 모드를 통해 사용자 친화적인 인터페이스를 제공합니다.