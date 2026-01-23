---
Language: Python  
tags:  
 - 추출 요약  
 - BERT  
 - 경량화 모델  
 - 자연어처리  
 - 딥러닝  
aliases:  
 - BERT 추출 요약  
 - 경량 BERT 요약  
 - DistilBERT 요약  
 - MobileBERT 요약  
 - BERTSUM 경량화  
url: https://github.com/chriskhanhtran/bert-extractive-summarization  
---
이 프로젝트는 저사양 장치에서 효율적으로 작동하도록 BERT 기반 추출 요약 모델을 경량화한 것입니다. DistilBERT와 MobileBERT를 CNN/DailyMail 데이터셋에 미세 조정하여 원본 BERT 성능 대비 45%~94% 수준을 유지하면서 4배 빠른 처리 속도와 작은 모델 크기를 구현했습니다.  

모델은 텍스트 입력에서 핵심 문장을 선택하여 요약을 생성하며, Heroku에서 호스팅되는 웹 데모와 Colab 노트북으로 쉽게 테스트할 수 있습니다. ROUGE 점수, 추론 시간, 모델 크기 비교 데이터를 통해 성능을 확인할 수 있습니다.