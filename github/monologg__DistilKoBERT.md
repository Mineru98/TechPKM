---
Language: Python  
tags:  
 - 한국어 BERT  
 - 경량화 모델  
 - 자연어 처리  
 - DistilBERT  
 - 트랜스포머  
aliases:  
 - DistilKoBERT  
 - 경량화 KoBERT  
 - 한국어 DistilBERT  
 - KoBERT 경량화 버전  
url: https://github.com/monologg/DistilKoBERT  
---  
DistilKoBERT는 KoBERT 모델의 경량화 버전으로, BERT의 12개 레이어를 3개로 축소하면서 성능을 유지하는 것을 목표로 합니다. 한국어 위키, 나무위키, 뉴스 등 약 10GB 규모의 코퍼스로 사전 학습되었으며, 기존 KoBERT 대비 모델 크기를 약 1/3로 줄이면서도 NSMC, NER, KorQuAD 등의 태스크에서 경쟁력 있는 성능을 보입니다. Hugging Face Transformers 라이브러리와 호환되어 쉽게 활용할 수 있으며, 동일한 토크나이저를 사용합니다.  

> 핵심 특징:  
> - 3계층 구조로 경량화  
> - KoBERT 대비 108MB 크기로 효율적  
> - 토큰 타입 임베딩 미지원  
> - `[CLS]` 토큰 활용 방식 변경 필요