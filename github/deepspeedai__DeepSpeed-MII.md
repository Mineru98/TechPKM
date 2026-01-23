---
Language: Python  
tags:  
 - 고속 추론  
 - 대규모 언어 모델  
 - 딥러닝 최적화  
 - 텍스트 생성  
 - GPU 병렬화  
aliases:  
 - DeepSpeed MII  
 - 고속 텍스트 생성  
 - MII 라이브러리  
 - DeepSpeed 추론 최적화  
url: https://github.com/deepspeedai/DeepSpeed-MII  
---
DeepSpeed-MII는 고성능 추론 최적화를 위한 오픈소스 라이브러리로, 대규모 언어 모델(LLM)의 고속 처리, 저지연, 비용 효율성을 목표로 합니다. 블록드 KV 캐싱, 연속 배치 처리, 동적 SplitFuse, CUDA 커널 등 핵심 기술을 활용하여 Llama, Mixtral, Phi-2 등의 모델에서 기존 시스템 대비 최대 2.5배 높은 처리량을 제공합니다. 8개 아키텍처(팔콘, 라마, 미스트랄 등)에 걸쳐 37,000개 이상의 모델을 지원하며, 텍스트 생성과 이미지 생성(예: Stable Diffusion) 작업에 적용 가능합니다. PyPI를 통해 간편하게 설치 가능하며, 단일 명령어로 비영구/영구 파이프라인 배포가 가능합니다.