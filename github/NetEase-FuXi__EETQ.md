---
Language: Python  
tags:  
 - INT8-양자화  
 - 트랜스포머-최적화  
 - PyTorch  
 - Flash-Attention  
 - 추론-가속화  
aliases:  
 - EasyEfficientQuantization  
 - EETQ-양자화  
 - 트랜스포머-양자화  
 - INT8-PTQ  
 - 퓨직-어텐션  
url: https://github.com/NetEase-FuXi/EETQ  
---
EETQ는 트랜스포머 모델의 효율적인 INT8 양자화와 추론을 지원하는 프레임워크입니다. 양자화 훈련 없이도 FasterTransformer 기반의 고성능 GEMM 커널과 Flash-Attention V2를 활용하여 모델 성능을 10~30% 향상시킵니다. PyTorch, HuggingFace Transformers, TGI 등 다양한 환경에서 한 줄의 코드로 적용 가능한 것이 특징입니다.  

주요 기능:  
1. INT8 양자화를 위한 PTQ(Post-Training Quantization) 지원  
2. Flash-Attention V2 기반의 최적화된 어텐션 레이어  
3. Transformers, TGI, LoRAX, vLLM 등 다양한 프레임워크 통합  
4. 양자화된 모델의 저장/재사용 기능 제공  

지원 환경: CUDA 11.4+, Python 3.8+, PyTorch 1.14.0+, Transformers 4.27.0+