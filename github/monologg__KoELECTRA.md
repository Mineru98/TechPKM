---
Language: Python  
tags:  
 - 한국어 NLP  
 - ELECTRA 모델  
 - 트랜스포머 라이브러리  
 - 사전 학습 언어 모델  
 - 텍스트 분류  
aliases:  
 - KoELECTRA  
 - 코일렉트라  
 - 한국어 ELECTRA  
url: https://github.com/monologg/KoELECTRA  
---
KoELECTRA는 한국어 텍스트로 사전 학습된 ELECTRA 기반 언어 모델입니다. 34GB의 한국어 데이터(뉴스, 위키, 문어/구어 말뭉치 등)로 학습되었으며, Base 및 Small 버전의 Discriminator와 Generator 모델을 제공합니다. Wordpiece 토크나이저를 사용하며, Hugging Face Transformers 라이브러리를 통해 Python에서 직접 활용 가능합니다. 한국어 텍스트 분류, 개체명 인식(NER), 문장 유사도 측정 등 다양한 NLP 태스크에서 우수한 성능을 입증했습니다.  

KoELECTRA-Base-v3는 NSMC(90.63% 정확도), KorNLI(82.24% 정확도), KorSTS(85.53 스피어만 상관계수) 등 주요 벤치마크에서 경쟁 모델 대비 최고 성능을 기록했습니다. Small 모델은 경량화된 버전으로, 리소스 제약 환경에서도 효율적인 한국어 처리가 가능합니다.