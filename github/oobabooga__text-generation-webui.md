---
Language: Python  
tags:  
 - Large Language Models  
 - Gradio UI  
 - GGUF 모델  
 - 이미지 생성  
 - 로컬 LLM  
aliases:  
 - text-generation-webui  
 - llama.cpp UI  
 - Oobabooga LLM 인터페이스  
 - 로컬 LLM 웹 UI  
url: https://github.com/oobabooga/text-generation-webui  
---  
Text Generation Web UI는 Large Language Models(LLM)를 위한 Gradio 기반 웹 인터페이스입니다. GGUF 모델을 포함한 다양한 로컬 LLM 백엔드를 지원하며, 이미지 생성(Z-Image-Turbo), 파일 첨부, 멀티모달 기능, OpenAI 호환 API 등을 제공합니다. 100% 오프라인에서 작동하며, 사용자 친화적인 UI와 확장 기능을 통해 맞춤형 생성형 AI 환경을 구축할 수 있습니다.  

주요 특징:  
- **다중 백엔드 지원**: llama.cpp, Transformers, ExLlamaV3 등  
- **이미지 생성**: 4비트/8비트 양자화 및 메타데이터 갤러리  
- **확장성**: 내장/사용자 정의 확장 기능 지원  
- **오프라인 운영**: 외부 의존성 없이 완전한 로컬 실행  
- **OpenAI 호환 API**: Chat 및 Completions 엔드포인트 제공  

설치 옵션:  
1. **포터블 빌드**: 압축 해제 후 즉시 실행 (Windows/Linux/macOS)  
2. **원클릭 설치**: 스크립트 자동 설치 및 Conda 환경 구성  
3. **수동 설치**: Docker 또는 Conda 기반 설치 가능  

프로젝트는 Hugging Face에서 모델을 다운로드하거나 CLI로 직접 가져올 수 있으며, 커뮤니티 및 문서 지원을 통해 지속적인 개선이 이루어지고 있습니다.