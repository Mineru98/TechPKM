---
Language: Python  
tags:  
 - llama.cpp  
 - Python 바인딩  
 - LLM  
 - OpenAI 호환  
 - 멀티모달  
aliases:  
 - llama-cpp-python  
 - llama.cpp 파이썬  
 - 로컬 LLM 서버  
url: https://github.com/abetlen/llama-cpp-python  
---
`llama-cpp-python`은 [ggerganov의 llama.cpp](https://github.com/ggerganov/llama.cpp) 라이브러리에 대한 Python 바인딩을 제공합니다. 이 프로젝트는 OpenAI와 호환되는 API를 지원하며, LangChain 및 LlamaIndex와의 통합이 가능합니다. CPU/GPU 가속화(백엔드: CUDA, OpenBLAS, Metal 등)를 지원하며, 멀티모달 모델(이미지 처리)과 함수 호출 기능을 포함합니다. 로컬 LLM 서버로도 활용 가능하며, Docker 이미지를 통해 배포할 수 있습니다.  

고수준 API는 텍스트 생성, 채팅 완료, JSON 스키마 응답 제약 등을 제공하며, 저수준 API는 C API에 직접 접근할 수 있도록 설계되었습니다. 모델 다운로드 및 관리를 위해 Hugging Face Hub와의 통합도 지원합니다. Python 3.8+ 환경에서 사용 가능합니다.