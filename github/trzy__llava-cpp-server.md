---
Language: C++
tags:
 - LLaVA
 - API 서버
 - llama.cpp
 - 멀티모달 AI
 - C++ HTTP 서버
aliases:
 - LLaVA C++ 서버
 - LLaVA-CPP-Server
 - LLaVA API 서버
 - 멀티모달 LLM 서버
url: https://github.com/trzy/llava-cpp-server
---
이 프로젝트는 llama.cpp 기반의 LLaVA 모델을 활용한 간단한 API 서버입니다. 로컬에서 실행되어 이미지 분석과 텍스트 프롬프트를 결합한 멀티모달 AI 기능을 제공하며, 웹 브라우저나 HTTP 클라이언트를 통해 상호작용할 수 있습니다. macOS에서 테스트되었으나 llama.cpp가 지원되는 모든 환경에서 빌드 및 운용이 가능합니다. `ggml-model`과 `mmproj-model` 파일을 다운로드한 후 서버 실행 파일을 통해 서비스를 시작할 수 있습니다.