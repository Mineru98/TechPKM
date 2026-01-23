---
Language: Python  
tags:  
 - Linear RNN  
 - Large Language Model  
 - HuggingFace 모델  
 - PyTorch 학습  
 - 텍스트 생성  
aliases:  
 - 선형화 LLM  
 - Linear OpenLM  
 - mistral-supra  
 - 선형 모델 학습  
url: https://github.com/tri-ml/linear_open_lm  
---
이 프로젝트는 대형 언어 모델(LLM)을 선형 RNN 구조로 변환하는 연구를 구현한 저장소입니다. 원본 OpenLM 저장소의 포크이며, Mistral-7B를 100B 토큰으로 업트레이닝한 Mistral-SUPRA 및 1.2T 토큰으로 학습한 Mamba-7B 모델을 제공합니다. 선형 모델 학습, 평가, 텍스트 생성 기능을 포함하며, HuggingFace를 통해 사전 학습된 모델을 사용할 수 있습니다. 주요 기술로는 PyTorch, FSDP 분산 학습, BPE 토크나이저가 활용되었습니다.