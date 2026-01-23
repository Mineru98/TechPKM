---
Language: Python  
tags:  
 - LLM 학습  
 - Triton 커널  
 - 메모리 최적화  
 - 딥러닝 프레임워크  
 - HuggingFace 통합  
aliases:  
 - Liger-Kernel  
 - Triton 고속화 커널  
 - LLM 훈련 가속  
url: https://github.com/linkedin/Liger-Kernel  
---  
**Liger Kernel**은 LLM(대형 언어 모델) 훈련을 위한 Triton 기반 커널 컬렉션입니다. 이 프로젝트는 멀티 GPU 훈련 처리량을 **20% 증가**시키고 메모리 사용량을 **60% 감소**시키며, Flash Attention, PyTorch FSDP, DeepSpeed 등과 호환됩니다. Hugging Face 모델과 통합 가능한 `RMSNorm`, `RoPE`, `SwiGLU`, `CrossEntropy` 등의 커널을 제공하며, DPO, ORPO 등 정렬 작업용 커널을 통해 **최대 80% 메모리 절약**을 지원합니다. 단일 코드 변경으로 모델 성능 향상이 가능하며, 커뮤니티 기여를 통해 지속적으로 확장됩니다.