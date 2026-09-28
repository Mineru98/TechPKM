---
Language: Python
tags:
 - LLM
 - NVIDIA-GB10
 - vLLM
 - 분산추론
 - NCCL
aliases:
 - SparkRing
 - SIRCL
 - 스파크링
url: https://github.com/FujitsuPolycom/sparkring
---
SparkRing는 NVIDIA GB10 기반 장치 2~4대를 다이렉트 어택 케이블로 연결하여 네트워크 스위치 없이 대규모 언어 모델을 실행하는 프로젝트입니다. SIRCL, RoCEnante, 패치된 NCCL을 통해 ConnectX-7 링크 상에서 집합 통신을 수행하며, vLLM과 SGLang을 지원하는 모델 프로파일(Qwen, GLM, MiMo, DeepSeek 등)과 원라인 설치 스크립트를 제공합니다.