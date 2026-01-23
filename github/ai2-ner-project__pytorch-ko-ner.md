---
Language: Python  
tags:  
 - 한국어 NER  
 - PLM 튜닝  
 - 개체명 인식  
 - KoBERT  
 - HuggingFace  
aliases:  
 - 한국어 개체명 인식기  
 - PLM 기반 NER  
 - KoBERT NER 튜닝  
 - 한국어 엔티티 인식  
url: https://github.com/example/plm-ner  
---
한국어 개체명 인식(NER)을 위한 PLM(Pre-trained Language Model) 파인튜닝 프로젝트입니다. 국립국어원 말뭉치 데이터를 활용해 15개 개체명 유형(인명, 지명, 문명 등)을 인식하는 모델을 구현했습니다. KLUE BERT/RoBERTa, KoBERT, KoELECTRA, KoBigBird 등 다양한 한국어 PLM을 비교 평가하고 앙상블 기법으로 성능을 개선했습니다. HuggingFace 라이브러리와 사용자 정의 전처리 파이프라인을 활용해 학습 및 추론 과정을 구현했습니다. 최종 평가에서 KLUE RoBERTa가 0.866의 F1 점수로 가장 우수한 성능을 보였습니다.