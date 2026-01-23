---
Language: Python  
tags:  
 - LoRA  
 - 자연어처리  
 - 파인튜닝  
 - LLaMA  
 - 오픈소스  
aliases:  
 - alpaca-lora  
 - 알파카-로라  
 - Stanford-Alpaca-LoRA  
url: https://github.com/tloen/alpaca-lora  
---
이 프로젝트는 Stanford Alpaca의 결과를 저랭크 적응(LoRA) 기법으로 재현하기 위한 코드와 자원을 제공합니다. 단일 RTX 4090 GPU에서 몇 시간 내에 훈련 가능한 경량화된 파인튜닝 솔루션을 구현하며, Hugging Face의 PEFT와 bitsandbytes 라이브러리를 활용합니다. 7B, 13B, 30B, 65B 모델 크기에 확장 가능하며, Raspberry Pi에서도 실행 가능한 수준의 효율성을 목표로 합니다. 오픈소스 LoRA 가중치 및 추론 스크립트를 포함하여 다양한 언어별 파인튜닝 모델을 지원합니다.