---
Language: Python  
tags:  
 - LLM 파인튜닝  
 - 강화학습  
 - VRAM 최적화  
aliases:  
 - Unsloth  
 - LLM 고속 학습  
url: https://github.com/unslothai/unsloth  
---
Unsloth는 다양한 대형 언어 모델(LLM)의 파인튜닝을 가속화하는 오픈소스 라이브러리로, VRAM 사용량을 최대 80%까지 감소시키며 기존 대비 최대 2배 빠른 학습 속도를 제공합니다. gpt-oss, Qwen, Gemma, Llama 등 주요 모델을 지원하며, 4비트/8비트 양자화, FP8 학습, 멀티모달 비전 모델 학습, TTS(텍스트-음성 변환) 등을 포함한 다양한 기능을 제공합니다. 사용자 친화적인 Colab 노트북과 Docker 환경을 통해 초보자도 쉽게 접근할 수 있습니다.  

Unsloth의 핵심 기술은 Triton 커널 기반의 메모리 효율적 처리와 배치 최적화 알고리즘으로, 500K 이상의 컨텍스트 길이도 지원합니다. Hugging Face, vLLM, llama.cpp 등과의 호환성을 통해 배포 및 추론까지 원활하게 수행할 수 있습니다. Linux, Windows, AMD/Intel GPU 등 다양한 플랫폼에서 작동하며, 커뮤니티 문서와 블로그, 튜토리얼을 통해 지속적인 기술 지원이 이루어집니다.