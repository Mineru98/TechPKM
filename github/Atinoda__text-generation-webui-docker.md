---
Language: Dockerfile
tags:
 - text-generation-webui
 - docker
 - NVIDIA
 - AMD
 - CPU
aliases:
 - text-generation-webui-docker
 - 텍스트-생성-웹UI-도커
 - oobabooga-도커
 - 생성형-AI-도커
url: https://github.com/Atinoda/text-generation-webui-docker
---
이 프로젝트는 [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui)를 도커 환경에서 쉽게 배포할 수 있도록 컨테이너화한 솔루션입니다. NVIDIA/AMD/Intel GPU 및 CPU 전용 버전을 제공하며, 확장 모듈 포함/제외 설정이 가능한 기본 버전과 경량 버전을 선택할 수 있습니다. 도커 컴포즈를 통해 로컬 서버(127.0.0.1:7860)로 빠르게 배포 및 관리할 수 있습니다.  

AMD GPU(ROCM) 및 Intel Arc GPU 지원은 실험적 기능이며, 확장 모듈의 경우 일부 호환성 문제가 있을 수 있습니다. 사전 빌드된 이미지는 Docker Hub에서 제공되며, 매일 자동 빌드되는 최신 버전(nightly)도 활용 가능합니다. 주요 사용 사례로는 생성형 AI 텍스트 모델 추론 서비스 구축이 포함됩니다.