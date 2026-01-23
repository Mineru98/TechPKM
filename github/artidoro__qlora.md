---
Language: Python  
tags:  
 - 양자화  
 - LLM 파인튜닝  
 - 4-bit 학습  
 - LoRA  
 - bitsandbytes  
aliases:  
 - QLoRA  
 - Low-Rank Adapters  
 - Guanaco 모델  
url: https://github.com/artidoro/qlora  
---
QLoRA는 4비트 양자화된 대형 언어 모델(LLM)을 효율적으로 파인튜닝하기 위한 기술로, 48GB GPU 한 대에서 65B 파라미터 모델을 파인튜닝할 수 있도록 메모리 사용량을 최적화합니다. 주요 혁신 기술인 4비트 정규화 부동소수점(NF4), 이중 양자화, 페이지드 옵티마이저를 활용해 성능을 유지하며 메모리를 절약합니다. 이 기술은 LLaMA, T5 등 다양한 모델 크기에 적용 가능하며, Vicuna 벤치마크에서 ChatGPT 수준의 99.3% 성능을 달성한 Guanaco 모델 시리즈를 포함합니다. MIT 라이선스로 배포되며, Hugging Face의 PEFT 및 transformers 라이브러리와 통합되어 있습니다.