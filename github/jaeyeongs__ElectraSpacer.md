---
Language: Python  
tags:  
 - 한국어 띄어쓰기  
 - ELECTRA 모델  
 - 자연어처리  
 - KoCharELECTRA  
 - 시퀀스 태깅  
aliases:  
 - ElectraSpacer  
 - 한국어 띄어쓰기 교정기  
 - 음절 단위 토크나이저  
url: https://github.com/jaeyeongs/research-develpoment/tree/main/Model/ElectraSpacer  
---  
ElectraSpacer는 KoCharELECTRA 모델을 기반으로 음절 단위 토큰화를 수행하는 한국어 자동 띄어쓰기 교정 도구입니다. 국립국어원 말뭉치를 활용해 훈련되었으며, 99%의 높은 정확도로 공백 없는 문장을 표준 규칙에 맞춰 교정합니다. `predict.py`를 통해 즉시 문장 교정이 가능하며, KoCharElectraTokenizer를 사용해 음절과 공백까지 세밀하게 태깅하는 것이 특징입니다.