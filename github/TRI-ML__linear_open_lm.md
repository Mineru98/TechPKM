---
Language: Python  
tags:  
 - 선형변환  
 - 언어모델  
 - 딥러닝  
 - 머신러닝  
 - 허깅페이스  
aliases:  
 - LinearOpenLM  
 - 선형LLM  
 - TRI-ML-LinearLM  
url: https://github.com/TRI-ML/linear_open_lm  
---
이 프로젝트는 대형 언어 모델(LLM)을 선형화하는 기법을 구현한 오픈소스 리포지토리입니다. 원본 OpenLM 저장소를 포크하여 [Linearizing Large Language Models](https://arxiv.org/abs/2405.06640) 논문의 방법론을 적용했습니다. 주요 기능으로는 Mistral-SUPRA 및 Mamba-7B 모델 제공, 선형 모델 훈련/평가/추론 스크립트 포함, HuggingFace 호환성 지원이 있습니다. 선형 변환된 모델은 기존 트랜스포머 기반 아키텍처를 RNN 구조로 변환하여 계산 효율성을 높이면서도 성능을 유지합니다.  

주요 특징:  
- 1B~7B 파라미터 규모의 선형 모델 지원  
- 사전 학습된 모델(Mistral-SUPRA, Mamba-7B) 제공  
- 훈련/평가/생성 스크립트 내장  
- HuggingFace 변환기와의 호환성  
- 다양한 벤치마크(HellaSwag, PIQA 등) 평가 지원