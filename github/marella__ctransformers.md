---
Language: Python
tags:
 - 트랜스포머
 - AI 모델
 - C/C++ 바인딩
aliases:
 - ctransformers
 - GGML 트랜스포머
url: https://github.com/marella/ctransformers
---
이 프로젝트는 GGML 라이브러리를 기반으로 C/C++로 구현된 트랜스포머 모델에 대한 파이썬 바인딩을 제공합니다. GPT-2, LLaMA, Falcon 등 다양한 모델을 지원하며 CUDA 및 Metal 가속을 통해 고성능 AI 추론이 가능합니다. 🤗 Transformers 및 LangChain과의 통합을 지원하며 로컬 또는 허깅페이스 허브에서 모델을 로드할 수 있습니다.  

MIT 라이선스로 배포되며 실험적인 GPTQ 모델 및 GPU 레이어 할당 기능을 포함합니다. 최대 컨텍스트 길이 조정과 스트리밍 생성도 지원합니다.