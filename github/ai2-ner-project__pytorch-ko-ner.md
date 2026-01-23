---
Language: Python  
tags:  
 - 한국어 NER  
 - PLM  
 - HuggingFace  
 - 개체명 인식  
 - 한국어 NLP  
aliases:  
 - 한국어 개체명 인식기  
 - PLM 기반 NER  
 - Ko-NER 모델  
 - 한국어 NLP 모델  
url: https://github.com/ai2-ner-project/pytorch-ko-ner  
---  
## 요약  
주요 한국어 PLM(언어 모델)을 미세 조정(fine-tuning)하여 15개 유형의 한국어 개체명(NER)을 인식하는 프로젝트입니다. 국립국어원 말뭉치 데이터셋을 활용하며, HuggingFace 라이브러리로 모델을 구현했습니다. klue/roberta-base 모델이 최고 성능(F1 0.866)을 보였으며, 데이터 전처리부터 학습, 평가까지 전체 파이프라인이 제공됩니다.  

### 핵심 특징  
- 5개 한국어 PLM(koBERT, klue-BERT/RoBERTa, KoELECTRA, BigBird) 비교 평가  
- 80만 문장 중 35만 문장으로 학습/평가  
- 개체명 미포함 문장 샘플링을 통한 데이터 균형 조정  
- 5-Fold 교차 검증 및 앙상블 추론 지원  
- Entity-level micro F1 기준 평가 지표 사용