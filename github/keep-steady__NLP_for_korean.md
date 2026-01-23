---
Language: Python  
tags:  
 - 한국어 자연어처리  
 - 토크나이저 비교  
 - konlpy  
 - subword 학습  
aliases:  
 - 한국어 NLP  
 - kr-tokenizer  
 - nlp_for_korean  
url: https://github.com/keep-steady/NLP_for_korean  
---  
이 프로젝트는 한국어 자연어처리를 위한 토크나이저 구현 및 성능 비교 실험을 목표로 합니다. Mecab 기반 전처리 후 Huggingface Tokenizers와 SentencePiece를 활용한 서브워드 학습 모델을 구축하고, konlpy 라이브러리 내 다양한 토크나이저(Hannanum, Kkma, Komoran, Okt)의 처리 속도와 결과를 비교 분석합니다. 특히 Okt 토크나이저가 단어 분해와 처리 속도 측면에서 우수한 성능을 보임으로써 한국어 처리에 적합함을 보여줍니다.