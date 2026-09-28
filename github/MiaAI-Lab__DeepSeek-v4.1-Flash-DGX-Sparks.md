---
Language: Python
tags:
 - LLM-serving
 - SGLang
 - DGX-Spark
 - DeepSeek
 - 분산추론
aliases:
 - DeepSeek-V4.1-Flash
 - DeepSeek V4.1 Flash DGX Sparks
 - DSV41
url: https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-DGX-Sparks/blob/main/README.md
---
이 프로젝트는 NVIDIA DGX Spark(GB10) 장비 3~4대를 ConnectX-7 RoCE 네트워크로 연결하여 DeepSeek-V4.1-Flash 대규모 언어 모델을 SGLang 기반으로 서빙하는 레시피입니다. MXFP4 전문가 가중치, FP8 dense 가중치, NVMe 상주 Engram 테이블, DSpark speculative decoding 등을 활용해 통합 메모리 환경의 제약을 극복하고, OpenAI 호환 엔드포인트를 통해 단일 노드 51 tok/s부터 4노드 TP=4 구성에서 최대 659 tok/s, 1M 토큰 컨텍스트까지 검증된 성능을 제공합니다.