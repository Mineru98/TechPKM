---
Language: Python  
tags:  
 - 추출적요약  
 - BERT  
 - DistilBERT  
 - MobileBERT  
 - NLP  
aliases:  
 - 경량BERT요약  
 - BERTSUM경량화  
 - 추출요약모델  
url: https://github.com/chriskhanhtran/bert-extractive-summarization  
---  
이 프로젝트는 저사양 장치에서도 효율적으로 작동하도록 BERT 기반 추출적 요약 모델을 경량화한 것입니다. DistilBERT와 MobileBERT를 CNN/DailyMail 데이터셋으로 파인튜닝하여 기존 BERT 대비 45%~75% 크기 감소와 2.7배 빠른 추론 속도를 달성하면서도 유사한 성능을 유지합니다. 허깅페이스 라이브러리와 사용자 정의 코드를 통해 구현되었으며, 실시간 웹 데모와 샘플 결과를 제공합니다.