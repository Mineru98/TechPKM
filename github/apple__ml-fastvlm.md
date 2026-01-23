---
Language: Python  
tags:  
 - Vision-Language Model  
 - Efficient Vision Encoding  
 - Mobile Optimization  
 - Image Processing  
 - CVPR 2025  
aliases:  
 - FastVLM  
 - FastViTHD  
 - LLaVA-FastViTHD  
 - Vision-Language Hybrid Encoder  
 - Efficient Image Tokenization  
url: https://github.com/haotian-liu/LLaVA  
---  
FastVLM은 고해상도 이미지 인코딩 시 출력 토큰 수를 줄이고 처리 시간을 크게 개선하는 하이브리드 비전 인코더 FastViTHD를 제안하는 프로젝트입니다. iOS 앱 데모를 통해 모바일 기기에서의 성능을 검증했으며, Qwen2-7B LLM 기반 모델은 기존 작품 대비 7.9배 빠른 TTFT(Time-to-First-Token)를 달성했습니다. 0.5B 모델 버전은 LLaVA-OneVision 대비 85배 빠른 TTFT와 3.4배 작은 인코더 크기를 특징으로 합니다. PyTorch 체크포인트와 Apple Silicon 호환 모델을 제공하며, CVPR 2025에 채택된 기술을 기반으로 합니다.