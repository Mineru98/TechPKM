---
Language: Python  
tags:  
 - 소형 언어 모델  
 - Open-Source LLM  
 - Slimpajama 데이터셋  
 - Pretraining  
 - 파인튜닝 기반 응용  
aliases:  
 - MicroLlama-300M  
 - 소형 라마 모델  
 - 300M 파라미터 모델  
url: https://github.com/keeeeenw/MicroLlama/blob/main/README.md  
---  
MicroLlama는 300M 파라미터 규모의 소형 언어 모델로, $500 예산 내에서 오픈소스 데이터셋(Slimpajama)과 도구를 활용해 처음부터 사전 학습된 모델입니다. 제한된 컴퓨팅 자원(4x Nvidia 4090)에서 50B 토큰으로 훈련되었으며, BERT 계열 모델 대비 우수한 성능을 보여 파인튜닝을 통한 응용(예: 텍스트 임베딩, 경량 챗봇)에 적합합니다. TinyLlama 프로젝트를 기반으로 데이터 처리 및 훈련 효율성을 개선했습니다.