---
Language: Python  
tags:  
 - 신경망 최적화  
 - Muon  
 - 딥러닝 옵티마이저  
 - PyTorch  
 - AdamW  
aliases:  
 - Muon 옵티마이저  
 - MuonWithAuxAdam  
 - 신경망 은닉층 최적화  
 - Muon 깃허브  
url: https://github.com/KellerJordan/Muon  
---  
Muon은 신경망의 은닉층 가중치를 최적화하기 위한 새로운 옵티마이저로, 임베딩 및 분류기 헤드 등 다른 파라미터에는 AdamW 사용을 권장합니다. CIFAR-10 및 트랜스포머 모델에서 빠른 훈련 속도와 우수한 성능을 입증했으며, 대규모 배치 및 모델 확장 시 안정적인 동작을 지원합니다. 주요 논문 및 벤치마크에서 기존 옵티마이저 대비 성능 향상을 확인했으며, Kimi.ai 등의 실제 프로젝트에서 활용되고 있습니다.