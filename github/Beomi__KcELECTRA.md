---
Language: Python  
tags:  
 - 한국어 NLP  
 - ELECTRA 모델  
 - 사용자 생성 텍스트  
 - 사전 학습 모델  
aliases:  
 - KcELECTRA  
 - 한국어 댓글 모델  
 - 사용자 생성 노이즈 텍스트 모델  
url: https://github.com/Beomi/KcELECTRA  
---
KcELECTRA는 온라인 뉴스 댓글과 대댓글 데이터로 학습된 한국어 ELECTRA 모델로, 사용자 생성 노이즈 텍스트(NSMC 등)에 특화된 성능을 보여줍니다. 기존 KcBERT 대비 확장된 데이터셋(45GB)과 vocab을 기반으로 대부분의 downstream task에서 1%p 이상의 성능 향상을 달성했습니다. Huggingface Transformers 라이브러리를 통해 간편하게 사용 가능하며, 구어체·신조어·오탈자 처리에 강점이 있습니다.  

(참고: 범용 작업에는 KoELECTRA가 더 적합할 수 있음)