---
Language: Python  
tags:  
 - 강화학습  
 - 트랜스포머  
 - 파인튜닝  
 - 허깅페이스  
 - 대규모언어모델  
aliases:  
 - 트랜스포머강화학습  
 - TRL  
 - GRPO  
 - DPO  
 - SFTTrainer  
url: https://github.com/huggingface/trl  
---  
TRL(Transformer Reinforcement Learning)은 허깅페이스 생태계의 트랜스포머 기반 파운데이션 모델을 사후 훈련하기 위한 라이브러리입니다. 지도학습 파인튜닝(SFT), 그룹 상대 정책 최적화(GRPO), 직접 선호 최적화(DPO) 등 다양한 강화학습 기법을 지원하며, 분산 학습과 하드웨어 확장을 위한 가속 기술을 통합했습니다. 대규모 언어모델의 효율적인 훈련을 위해 PEFT(LoRA/QLoRA) 및 최적화된 커널(Unsloth)과 연동되어, 단일 GPU부터 멀티노드 클러스터 환경까지 유연하게 적용할 수 있습니다. CLI를 통해 코드 작성 없이도 파인튜닝을 수행할 수 있는 기능을 제공합니다.