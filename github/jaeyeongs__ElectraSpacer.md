---
Language: Python  
tags:  
 - 한국어 띄어쓰기  
 - NLP 모델  
 - ELECTRA  
 - KoCharELECTRA  
 - 자동 띄어쓰기  
aliases:  
 - ElectraSpacer  
 - 한국어 띄어쓰기 모델  
 - KoCharELECTRA 띄어쓰기  
url: https://github.com/jaeyeongs/ElectraSpacer  
---  
한국어 자동 띄어쓰기 교정 모델인 ElectraSpacer에 대한 설명입니다. KoCharELECTRA 기반 모델을 활용해 음절 단위 토큰화를 수행하며, 국립국어원 말뭉치 데이터를 학습하여 높은 정확도(99%)와 F1 점수(98%)를 달성했습니다. 잘못된 띄어쓰기 문장을 올바른 형식으로 변환하는 데 특화된 NLP 프로젝트입니다.  

> 📌 주요 기능:  
> - `predict.py`를 통한 실시간 띄어쓰기 교정  
> - JSON/CSV 형식의 학습 데이터 지원  
> - '모두의 말뭉치' 기반 문법성 판단 데이터 활용