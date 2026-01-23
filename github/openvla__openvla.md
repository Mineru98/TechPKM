---
Language: Python  
tags:  
 - Vision-Language-Action 모델  
 - 로봇 조작  
 - 오픈소스  
 - PyTorch  
 - HuggingFace  
aliases:  
 - OpenVLA  
 - OpenVLA-7b  
 - OpenVLA-v01-7b  
url: https://github.com/openvla/openvla  
---  
OpenVLA는 로봇 조작을 위한 오픈소스 비전-언어-행동(VLA) 모델입니다. PyTorch FSDP와 Flash-Attention을 활용해 1B~34B 파라미터 규모의 모델을 효율적으로 학습 및 미세 조정하며, Open X-Embodiment 데이터셋 혼합을 지원합니다. HuggingFace를 통해 사전 학습된 `openvla-7b` 및 `openvla-v01-7b` 모델을 제공하며, BridgeData V2 및 LIBERO 시뮬레이션 벤치마크에서의 평가 방법을 포함합니다. LoRA 및 전체 미세 조정 옵션을 통해 새로운 작업 및 로봇 플랫폼에 맞춰 적용 가능합니다.