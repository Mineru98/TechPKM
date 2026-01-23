---
Language: Python  
tags:  
 - 대규모언어모델  
 - 텍스트생성  
 - 로컬AI  
aliases:  
 - text-generation-webui  
 - 로컬LLMUI  
 - 대규모언어모델웹UI  
url: https://github.com/oobabooga/text-generation-webui  
---  
Gradio 기반의 대규모 언어 모델(Large Language Models, LLM)을 위한 웹 인터페이스입니다. llama.cpp, Transformers, ExLlamaV2/V3, TensorRT-LLM 등 다양한 백엔드를 지원하며, 오프라인 환경에서 완전히 작동하는 프라이버시 보호형 UI입니다. 이미지 생성, 파일 첨부, 웹 검색, API 연동, 확장 기능 등 다양한 기능을 제공하며, 사용자 친화적인 인터페이스와 함께 설치 편의성을 강점으로 합니다. macOS, Linux, Windows에서 사용 가능하며, 휴대용 빌드 또는 원클릭 설치 옵션을 통해 쉽게 시작할 수 있습니다.  

- **핵심 기능**: 이미지 생성(Z-Image-Turbo), 텍스트 생성(다양한 샘플링 파라미터), 파일 첨부(텍스트/PDF/DOCX), 멀티모달 모델 지원, OpenAI 호환 API  
- **기술 스택**: Python, Gradio, GGUF 모델  
- **사용 시나리오**: 로컬 환경에서 프라이버시 보장형 LLM 활용, 연구/개인용 생성형 AI 테스트베드  
- **특징**: 오프라인 작동, 사용자 정의 확장 지원, 다크/라이트 테마, 자동 프롬프트 포맷팅(Jinja2)