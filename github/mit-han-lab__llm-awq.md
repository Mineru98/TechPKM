---
Language: Python  
tags:  
 - LLM 압축  
 - 양자화  
 - 에지 컴퓨팅  
 - 멀티모달 모델  
 - PyTorch  
aliases:  
 - AWQ  
 - Activation-aware Weight Quantization  
 - TinyChat  
url: https://github.com/mit-han-lab/llm-awq  
---  
MIT Han Lab의 AWQ(Activation-aware Weight Quantization)는 대규모 언어 모델(LLM) 및 멀티모달 모델(VLM)의 효율적인 압축과 가속화를 위한 기술입니다. INT3/4 비트 양자화를 적용하여 정확도와 성능을 유지하면서 메모리 사용량을 줄이고, 에지 장치에서의 추론 속도를 개선합니다. TinyChat과 통합되어 Jetson Orin 같은 저사양 장치에서도 Llama-3, VILA 등 대형 모델의 4비트 추론이 가능하며, Hugging Face, TensorRT-LLM 등 다양한 플랫폼에 통합되었습니다.  

핵심 기능으로는 양자화 검색, 사전 계산된 모델 저장소, CUDA 기반 고속 커널 구현, 멀티이미지 입력 지원 등이 포함됩니다. MLSys 2024 최우수 논문상을 수상했으며, LLaMA, Vicuna, VILA 등 다양한 모델 패밀리를 지원합니다.