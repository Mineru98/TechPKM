---
Language: C/C++  
tags:  
 - LLM 추론  
 - 로컬 AI  
 - 하드웨어 최적화  
 - GGUF 형식  
 - 오픈소스  
aliases:  
 - llama.cpp  
 - ggml-org/llama.cpp  
 - 로컬 LLM 서버  
 - GGUF 모델 변환  
url: https://github.com/ggml-org/llama.cpp  
---  
`llama.cpp`는 다양한 하드웨어에서 최소한의 설정으로 고성능 LLM 추론을 가능하게 하는 C/C++ 프로젝트입니다. 주요 목표는 애플 실리콘, x86, RISC-V 아키텍처 및 NVIDIA/AMD GPU를 포함한 광범위한 장치에서 효율적인 추론 환경을 제공하는 것입니다. 1.5~8비트 양자화, CUDA/Vulkan 지원, CPU+GPU 하이브리드 추론 등 다양한 최적화 기법을 포함하며, GGUF 형식의 모델 파일 관리를 위한 도구도 제공합니다. OpenAI 호환 API 서버(`llama-server`)와 CLI 도구(`llama-cli`)를 통해 쉽게 활용할 수 있으며, 100개 이상의 오픈소스 언어 모델을 지원합니다.  

```sh
# 로컬 모델 파일 사용 예시
llama-cli -m my_model.gguf

# 허깅페이스에서 모델 다운로드 및 실행
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF

# OpenAI 호환 API 서버 실행
llama-server -hf ggml-org/gemma-3-1b-it-GGUF
```