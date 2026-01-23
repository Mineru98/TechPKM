---
Language: Python  
tags:  
 - 한국어 혐오발언 탐지  
 - LoRA 파인튜닝  
 - GPT-NeoX  
aliases:  
 - KoreanHateSpeech 분류기  
 - 한국어 혐오발언 이진분류  
 - qlora-혐오발언  
url: https://github.com/calisolo/KoreanHateSpeech_qlora  
---  
이 프로젝트는 한국어 혐오발언 탐지를 위한 인과적 모델 기반 이진 분류기 구현 코드입니다. 국립국어원과 모두의 말뭉치 데이터를 활용하며, Polyglot-Ko 1.3B 모델에 LoRA(QLoRA) 기법을 적용해 파라미터 효율적인 파인튜닝을 수행합니다. HuggingFace PEFT 라이브러리와 한국어 특화 언어모델을 결합한 혐오발언 분류 솔루션입니다.