---
Language: Python  
tags:  
 - 한국어 임베딩  
 - 자연어 처리  
 - Word2Vec  
 - 딥러닝  
 - OOV 해결  
aliases:  
 - kor2vec  
 - 한국어 임베딩 모델  
 - char-word 임베딩  
url: https://github.com/naver/kor2vec  
---  
한국어 텍스트를 교착어 특성에 맞춰 OOV(Out-Of-Vocabulary) 문제 없이 처리하는 임베딩 모델입니다. CNN 기반 Char-Word 인코더로 형태소 분석 없이도 문자 수준에서 문맥을 포착하며, Skip-gram 방식으로 학습됩니다. NLP 파이프라인에서 토크나이징 병목 현상을 해결하고 토큰화 오류를 방지하는 것이 핵심 목표입니다. PyTorch와 통합 가능한 구조로 설계되어 다양한 딥러닝 모델에 직접 적용이 가능합니다.