---
Language: Python  
tags:  
 - Attention 메커니즘  
 - 고성능 딥러닝  
 - GPU 최적화  
aliases:  
 - FlashAttention  
 - FlashAttention-2  
 - FlashAttention-3  
url: https://github.com/Dao-AILab/flash-attention  
---  
이 프로젝트는 FlashAttention 및 FlashAttention-2 논문을 기반으로 한 공식 구현체로, IO 인식 기반의 빠르고 메모리 효율적인 정확한 어텐션 메커니즘을 제공합니다. Hopper GPU(H100 등)를 위한 베타 버전인 FlashAttention-3도 포함되어 있으며, FP16/BF16/FP8 연산을 지원합니다. PyTorch 2.2 이상과 CUDA/ROCm 툴킷이 필요하며, 다양한 GPU 아키텍처(Ampere, Ada, Hopper 등)에서 동작합니다.  

주요 기능으로는 멀티쿼리/그룹드쿼리 어텐션, 슬라이딩 윈도우 로컬 어텐션, ALiBi 편향, 페이징 KV 캐시, 소프트캡핑 등이 포함됩니다. Triton 및 Composable Kernel 백엔드를 통해 AMD ROCm GPU도 지원하며, MLPerf 벤치마크에서 검증된 성능을 제공합니다.  

테스트 스위트는 PyTorch 기준 구현과의 출력/그래디언트 일치성을 검증하며, GPT 모델 전체 구현 및 훈련 스크립트도 포함되어 있습니다. 연구 논문 인용 시 @inproceedings{dao2022flashattention}, @inproceedings{dao2023flashattention2}를 권장합니다.