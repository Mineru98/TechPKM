---
Language: Python  
tags:  
 - 상태-공간 모델  
 - Mixture of Experts  
 - Mamba 아키텍처  
 - 딥러닝 추론  
 - 저지연 생성  
aliases:  
 - BlackMamba  
 - SSM-MoE  
 - 저비용 고성능 시퀀스 모델  
url: https://github.com/Zyphra/BlackMamba  
---  
BlackMamba는 상태-공간 모델(SSM)과 Mixture of Experts(MoE)를 결합한 혁신적인 아키텍처로, Mamba와 Switch Transformer 기술을 기반으로 합니다. 이 모델은 시퀀스 길이에 대해 선형 계산 복잡도를 유지하면서도 기존 트랜스포머 및 MoE 모델 대비 빠른 생성 및 추론 속도를 제공합니다. GitHub 저장소에는 사전 학습된 모델(340M/1.5B, 630M/2.8B 파라미터)과 PyTorch 기반 추론 코드가 포함되어 있으며, 저비용 고성능 시퀀스 처리 솔루션으로 설계되었습니다.  

> 요약: 상태-공간 모델과 전문가 혼합(MoE)을 결합한 고성능·저지연 시퀀스 모델 솔루션. 선형 복잡도 특성으로 효율적인 장기 시퀀스 처리 가능.