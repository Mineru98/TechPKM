---
Language: Python  
tags:  
 - 시계열 예측  
 - 파운데이션 모델  
 - Google Research  
 - 딥러닝  
 - 시계열 분석  
aliases:  
 - TimesFM  
 - Time Series Foundation Model  
 - 시계열 파운데이션 모델  
url: https://github.com/google-research/timesfm  
---  
TimesFM은 Google Research에서 개발한 시계열 예측을 위한 사전 훈련된 파운데이션 모델입니다. TimesFM 2.5 버전은 200M 파라미터를 사용하며, 최대 16k의 컨텍스트 길이와 연속적인 분위수 예측을 지원합니다. 이 모델은 PyTorch 및 Flax 백엔드를 사용할 수 있으며, `XReg`를 통한 공변량 지원 기능이 있습니다. 시계열 데이터의 다양한 특성에 맞춰 점 예측 및 분위수 예측을 수행할 수 있습니다.