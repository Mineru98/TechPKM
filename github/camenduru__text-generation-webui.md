---
Language: Python  
tags:  
 - LLM  
 - 텍스트 생성  
 - Gradio UI  
aliases:  
 - Text Generation Web UI  
 - 텍스트 생성 웹 UI  
 - oobabooga  
url: https://github.com/camenduru/text-generation-webui  
---  
대규모 언어 모델(LLM)을 위한 Gradio 기반 웹 인터페이스입니다. 다양한 모델 백엔드(Transformers, llama.cpp, ExLlamaV2 등)와 3가지 인터페이스 모드(기본, 노트북, 채팅)를 지원하며, LoRA, OpenAI 호환 API, 멀티모달 파이프라인, 음성 출력/입력 등 확장 기능을 제공합니다. Stable Diffusion의 웹 UI와 유사한 사용자 경험을 목표로 합니다.  

주요 기능:  
- 다양한 모델 백엔드 지원  
- LoRA 학습/동적 로딩  
- OpenAI 호환 API 서버  
- 확장 기능(음성 출력, 벡터 DB, 멀티모달 등)  
- 3가지 인터페이스 모드(기본/노트북/채팅)  
- 캐릭터 기반 채팅 및 정밀한 프롬프트 템플릿  
- AMD/NVIDIA/CPU 호환 설치 옵션  

Docker, 수동 설치, 자동 설치 스크립트 등 다양한 배포 방식을 지원합니다.