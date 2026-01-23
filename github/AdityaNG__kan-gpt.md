---
Language: Python  
tags:  
 - 언어모델링  
 - KAN  
 - GPT  
 - PyTorch  
 - 딥러닝  
aliases:  
 - KAN-GPT  
 - KAN 기반 GPT  
url: https://github.com/AdityaNG/kan-gpt  
---  
KAN-GPT는 콜모고로프-아르놀드 네트워크(KAN)를 활용하여 언어 모델링을 수행하는 PyTorch 기반 GPT 구현 프로젝트입니다. 기존의 MLP 기반 GPT와 비교하여 KAN의 표현력 향상을 실험적으로 검증하며, 웹텍스트 및 tiny shakespeare 데이터셋에서 학습 가능한 오픈소스 모델을 제공합니다.  

주요 특징으로는 PyPI를 통한 간편 설치, 훈련/추론 스크립트, W&B(Weights & Biases) 통합 체크포인트 관리 기능을 포함합니다. 현재는 KAN과 MLP 아키텍처의 성능 비교 실험 중이며, 향후 모델 가중치 자동 다운로드 및 PyTorch Lightning 통합 등의 확장 계획이 있습니다.