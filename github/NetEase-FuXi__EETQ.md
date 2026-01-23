---
Language: Python  
tags:  
 - 모델 양자화  
 - 트랜스포머 최적화  
 - PyTorch  
 - Flash-Attention  
 - INT8 양자화  
aliases:  
 - EETQ  
 - EETQ-양자화  
 - 트랜스포머 양자화  
 - EETQ-최적화  
url: https://github.com/NetEase-FuXi/EETQ  
---  
EETQ는 트랜스포머 모델을 위한 효율적이고 간편한 양자화 도구입니다. INT8 양자화를 통해 모델 성능을 유지하면서도 추론 속도를 10~30% 개선하며, Flash-Attention V2를 활용한 어텐션 레이어 최적화 기능을 제공합니다. PyTorch 모델과 호환되어 단일 코드 라인으로 적용 가능하며, Hugging Face Transformers, TGI, LoRAX 등 다양한 프레임워크에서 활용할 수 있습니다.  

주요 기능으로는 훈련 없이 적용 가능한 PTQ(Post-Training Quantization), FasterTransformer의 고성능 GEMM 커널 통합, 그리고 다양한 하드웨어 환경에서의 설치 및 사용 편의성을 포함합니다. 모델 크기와 계산 비용을 줄이면서 실시간 추론 요구사항을 충족하는 데 적합합니다.