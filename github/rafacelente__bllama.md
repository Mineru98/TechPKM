---
Language: Python  
tags:  
 - 1비트 LLM  
 - 양자화 추론  
 - PyTorch Lightning  
 - LLaMa 모델  
 - 비트선형 계층  
aliases:  
 - bLLaMa  
 - 비트라마  
 - 1.58비트 LLM  
 - BitLinear 모델  
url: https://github.com/rafacelente/bllama  
---
bLLaMa는 1.58비트 LLaMa 모델로, 훈련 시 `fp32` 모드와 추론 시 `int8` 양자화 모드를 지원하는 BitLinear 계층을 특징으로 합니다. 이 프로젝트는 PyTorch Lightning 기반의 경량화 LLM 구현체로, 셰익스피어/위키텍스트 데이터셋과 같은 텍스트 데이터로 훈련 및 추론이 가능합니다. 양자화된 추론 시 오프라인 가중치 변환이 필요하며, 현재 모델 체크포인트는 공개되지 않았습니다. 주요 개발 과제로는 KV 캐시, 모델 분산 훈련, 사용자 정의 저장 방식 등이 있습니다.  

요약: bLLaMa는 1.58비트 LLaMa 모델을 기반으로 한 경량화 LLM 구현체로, 훈련 시 전체 정밀도(`fp32`)와 추론 시 양자화된 `int8` 모드를 지원하는 BitLinear 계층을 특징으로 합니다. PyTorch Lightning을 활용하여 GPU에서 훈련 및 추론이 가능하며, 현재 작은 데이터셋(예: 셰익스피어, 위키텍스트)으로 검증되었습니다. 모델 체크포인트는 아직 공개되지 않았으며, 향후 KV 캐시 및 분산 훈련 최적화가 계획되어 있습니다.