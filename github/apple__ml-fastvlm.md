---
Language: Python  
tags:  
 - Vision-Language Models  
 - Efficient Vision Encoding  
 - Mobile AI  
 - CVPR 2025  
 - Hybrid Vision Encoder  
aliases:  
 - FastVLM  
 - 빠른 비전 언어 모델  
 - FastViTHD  
url: https://github.com/apple/ml-fastvlm  
---
FastVLM은 고해상도 이미지 인코딩 시 토큰 수를 줄이고 처리 속도를 크게 개선한 **FastViTHD** 하이브리드 비전 인코더를 제안한 프로젝트입니다. Apple의 CVPR 2025 논문 기반의 이 모델은 기존 LLaVA-OneVision 대비 85배 빠른 TTFT(Time-to-First-Token)와 3.4배 작은 인코더 크기를 구현하며, Qwen2-7B LLM과 결합한 대형 모델은 최근 연구 대비 7.9배 빠른 성능을 보입니다. iOS 데모 앱을 통해 모바일 환경 최적화를 입증했으며, 이미지 설명, 객체 카운팅 등 다양한 비전-언어 태스크에 적용 가능합니다.