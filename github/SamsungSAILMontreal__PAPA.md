---
Language: Python  
tags:  
 - 모델 평균화  
 - 머신러닝 연구  
 - CIFAR-10/100  
 - ImageNet  
 - 앙상블 기법  
aliases:  
 - PAPA  
 - PopulAtion Parameter Averaging  
 - 모델 인구 평균화  
 - 파라미터 앙상블  
url: https://github.com/AlexiaJM/recombine_nets  
---  
PopulAtion Parameter Averaging (PAPA)은 모델 집단을 훈련하며 주기적으로 평균화하여 단일 강력한 모델을 얻는 알고리즘입니다. 이 프로젝트는 TMLR에 게재된 논문을 공식적으로 구현한 것으로, 단일 모델 훈련보다 향상된 성능을 제공합니다. CIFAR-10/100, ImageNet 데이터셋에서 검증되었으며, 다양한 정규화 기법(믹스업, 라벨 스무딩 등)을 결합한 실험 환경을 지원합니다.  

PAPA는 주기적으로 모델을 평균화(PAPA-all)하거나 점진적으로 평균에 수렴(PAPA-gradual)하는 방식을 포함하며, 병렬 GPU 훈련을 통한 확장성을 고려했습니다. 연구 재현을 위해 실험 스크립트와 하이퍼파라미터 설정을 상세히 제공합니다.