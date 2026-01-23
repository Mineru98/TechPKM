---
Language: Python  
tags:  
 - 분산 학습  
 - PyTorch 확장  
 - 대규모 모델 훈련  
 - 고성능 컴퓨팅  
 - 모듈식 설계  
aliases:  
 - FairScale  
 - 페어스케일  
 - FSDP  
 - PyTorch 확장 라이브러리  
 - 대규모 훈련  
url: https://github.com/facebookresearch/fairscale  
---  
FairScale은 고성능 및 대규모 모델 훈련을 위한 PyTorch 확장 라이브러리입니다. 제한된 자원으로 모델을 확장하는 연구자들을 위해 최신 분산 훈련 기법을 모듈식 API로 제공하며, 사용성, 모듈성, 성능을 핵심 가치로 설계되었습니다. 특히 FSDP(Fully Sharded Data Parallel)는 대규모 신경망 모델을 위한 추천 기법으로, 현재는 PyTorch 공식 라이브러리로 편입되었습니다.  

이 프로젝트는 PyTorch의 기본 기능을 확장하면서 SOTA(scaling techniques) 기법을 쉽게 적용할 수 있도록 하며, 커뮤니티에서 널리 사용되는 다양한 라이브러리를 통합하여 유연한 훈련 환경을 지원합니다.