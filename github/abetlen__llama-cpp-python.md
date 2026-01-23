---
Language: Python  
tags:  
 - llama-cpp  
 - LLM 바인딩  
 - OpenAI 호환  
 - 하드웨어 가속  
 - 멀티모달  
aliases:  
 - llama-cpp-python  
 - llama.cpp 파이썬  
 - 로컬 LLM 서버  
url: https://github.com/abetlen/llama-cpp-python  
---
`llama-cpp-python`은 [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) 라이브러리의 Python 바인딩으로, 로컬에서 LLM(대형 언어 모델) 추론 및 OpenAI 호환 서버 기능을 제공합니다. 이 패키지는 저수준 C API 접근과 함께, 텍스트 생성, 채팅 완료, 함수 호출, JSON 스키마 생성, 멀티모달 모델 지원 등 다양한 고수준 API를 제공합니다. CUDA, Metal, OpenBLAS 등 다양한 하드웨어 가속 백엔드를 지원하며, Docker 이미지 및 사전 빌드 휠을 통해 설치가 용이합니다. LangChain, LlamaIndex와의 호환성을 갖추어 기존 LLM 통합 프레임워크에 쉽게 적용할 수 있습니다.