---
Language: Python  
tags:  
 - 한국어 NLP  
 - ELECTRA 모델  
 - 사용자 생성 텍스트  
 - 트랜스포머  
 - 파인튜닝  
aliases:  
 - KcELECTRA  
 - 한국어 댓글 ELECTRA  
 - User-Generated Noisy Text 모델  
url: https://github.com/Beomi/KcELECTRA  
---  
KcELECTRA는 한국어 온라인 뉴스 댓글 및 대댓글로 학습된 ELECTRA 기반 언어 모델입니다. 사용자 생성 텍스트(User-Generated Noisy Text)에 특화된 성능을 목표로 하며, 기존 KcBERT 대비 확장된 데이터(3.4억 건)와 vocab을 활용해 성능을 향상시켰습니다. NSMC, NER, NLI 등 다양한 한국어 다운스트림 태스크에서 우수한 성능을 보이며, Huggingface Transformers를 통해 쉽게 사용 가능합니다. 일반 코퍼스 기반 모델보다 구어체 및 노이즈가 많은 텍스트에 강점을 가집니다.