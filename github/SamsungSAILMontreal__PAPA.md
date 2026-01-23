---
Language: Python
tags:
 - 모델 앙상블
 - 파라미터 평균화
 - 머신러닝 연구
 - PyTorch
 - 이미지 분류
aliases:
 - PAPA
 - PopulAtion Parameter Averaging
 - 모델 인구 평균화
 - PAPA-gradual
 - PAPA-all
url: https://github.com/SamsungSAILMontreal/PAPA
---
PopulAtion Parameter Averaging (PAPA)는 모델 집단의 파라미터를 주기적으로 평균화하여 단일 강건한 모델을 얻는 알고리즘 구현입니다. TMLR에 게재된 논문을 바탕으로, 다양한 정규화 전략을 적용한 모델 집단을 훈련시킨 후 평균화(PAPA-all, PAPA-2) 또는 점진적으로 평균(EMA)으로 유도하는 방식을 지원합니다. CIFAR-10/100 및 ImageNet 데이터셋에서 실험 가능하며, PyTorch 기반으로 구현되어 있습니다. 모델 성능을 향상시키기 위해 REPAIR 기법 및 병렬 훈련을 옵션으로 제공합니다.