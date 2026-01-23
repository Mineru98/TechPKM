---
Language: Python  
tags:  
 - Mixtral-8x7B  
 - 모델 추론 최적화  
 - MoE 전문가 오프로딩  
 - 양자화 기술  
 - GPU 메모리 관리  
aliases:  
 - Mixtral 오프로딩  
 - Mixtral 추론 효율화  
 - MoE 오프로딩 전략  
url: https://github.com/dvmazur/mixtral-offloading  
---  
이 프로젝트는 Mixtral-8x7B 모델의 효율적인 추론을 위한 기술을 구현합니다. HQQ 기반 혼합 양자화와 MoE 전문가 오프로딩 전략을 결합해 GPU와 CPU 메모리 사용을 최적화하며, LRU 캐시 메커니즘으로 인접 토큰 처리 시 GPU-RAM 통신 오버헤드를 줄입니다. 향후 다른 양자화 방법과 전문가 사전 페치 기능 추가를 계획 중이며, 현재 Colab 노트북을 통해 데모 실행이 가능합니다. 기술 보고서는 arXiv에서 확인 가능합니다.