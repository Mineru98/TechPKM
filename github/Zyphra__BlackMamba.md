---
Language: Python  
tags:  
 - 상태 공간 모델  
 - Mixture of Experts  
 - 딥러닝 아키텍처  
 - 자연어 처리  
 - 저지연 생성  
aliases:  
 - BlackMamba-SSM-MoE  
 - 블랙맘바 모델  
 - Mamba MoE 결합  
 - 상태 공간 전문가 혼합  
url: https://github.com/Zyphra/BlackMamba  
---  
BlackMamba는 상태 공간 모델(SSM)과 전문가 혼합(MoE) 아키텍처를 결합한 혁신적인 딥러닝 모델입니다. Mamba SSM 블록과 Switch Transformer 기반 MoE를 활용해 기존 트랜스포머 및 SSM 모델 대비 우수한 속도와 선형 계산 복잡도를 제공합니다. 이 저장소는 해당 모델의 추론 코드와 사전 학습된 가중치(340M/1.5B, 630M/2.8B)를 포함하며, 저지연 생성 및 추론에 최적화되었습니다. 주요 적용 분야는 자연어 처리와 같은 시퀀스 모델링 작업입니다.