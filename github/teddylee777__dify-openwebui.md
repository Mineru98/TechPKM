---
Language: Shell
tags:
 - 설치 가이드
 - Docker
 - Ollama
 - Dify
 - OpenWebUI
aliases:
 - Dify OpenWebUI 설치
 - Dify Ollama 통합
 - 로컬 LLM 설치
 - AI 워크플로우 구성
url: https://github.com/teddylee777/dify-openwebui
---
이 프로젝트는 Dify와 OpenWebUI를 Docker, Ollama와 함께 설치하여 로컬에서 AI 워크플로우를 구성하는 방법을 단계별로 설명합니다. 주요 기술 스택으로 Docker 컨테이너 환경, Ollama LLM 실행, OpenWebUI 웹 인터페이스가 통합되어 있으며, Git 기반 프로젝트 관리와 포트 설정, API 연결 등 전체 시스템 구성 절차를 다룹니다.  

> 📌 **핵심 특징**:  
> - **로컬 LLM 실행**: Ollama를 통해 `bge-m3`, `dnotitia/dna` 등 모델 활용  
> - **통합 워크플로우**: Dify의 DSL 파일과 OpenWebUI 파이프라인 연동  
> - **다중 플랫폼 지원**: Ubuntu, Windows, MacOS 설치 가이드 제공  
> - **확장성**: 커스텀 모델 추가 및 API 키 관리 기능 포함