---
Language: Python  
tags:  
 - Vision-Language-Action  
 - 로보틱 조작  
 - 딥러닝  
 - HuggingFace  
 - PyTorch  
aliases:  
 - OpenVLA  
 - Open Vision-Language-Action  
 - 로봇 제어 모델  
url: https://github.com/openvla/openvla  
---
OpenVLA는 일반 로봇 조작을 위한 오픈소스 비전-언어-행동(VLA) 모델 및 학습 코드베이스입니다. Open X-Embodiment 데이터셋과 같은 RLDS 형식의 다양한 데이터셋 혼합을 지원하며, LoRA 및 전체 미세 조정과 같은 효율적인 방법으로 1B~34B 파라미터 모델을 확장할 수 있습니다. PyTorch FSDP와 Flash-Attention을 활용해 분산 학습을 지원하며, HuggingFace Transformers와 호환되는 경량 인터페이스를 제공합니다. BridgeData V2 및 LIBERO 시뮬레이션 벤치마크와 같은 로봇 환경에서 제로샷 또는 미세 조정 후 행동 예측이 가능합니다. Llama-2 기반의 사전 훈련 모델을 사용하며, MIT 라이선스로 공개됩니다.