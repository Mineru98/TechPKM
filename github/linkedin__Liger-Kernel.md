---
Language: Python  
tags:  
 - LLM 학습  
 - Triton 커널  
 - 메모리 최적화  
 - 다중 GPU  
 - 오픈소스  
aliases:  
 - Liger-Kernel  
 - LLM 훈련 최적화  
 - Triton 기반 커널  
url: https://github.com/linkedin/Liger-Kernel  
---  
Liger Kernel은 LLM(대규모 언어 모델) 훈련을 위해 특화된 Triton 커널 컬렉션입니다. 20%의 훈련 처리량 향상과 60%의 메모리 감소를 달성하며, Hugging Face 호환 `RMSNorm`, `RoPE`, `SwiGLU`, `CrossEntropy` 등의 커널을 제공합니다. Flash Attention, PyTorch FSDP, DeepSpeed와의 호환성을 바탕으로 다중 GPU 환경에서 효율적인 학습을 지원합니다. 또한 DPO, ORPO 등의 정렬 및 증류 작업을 위한 80% 메모리 절감 커널도 포함되어 있습니다. 단일 코드 변경으로 적용 가능하며, 커뮤니티 기여를 통해 지속적으로 확장됩니다.