---
Language: Python  
tags:  
 - 한국어-분류  
 - NLP  
 - 텍스트-분류  
 - 딥러닝  
 - Mecab  
aliases:  
 - 한국어 뉴스 분류  
 - 뉴스 카테고리 분류기  
 - korean-news-classification  
url: https://github.com/Moog303/Korean_News_Classification  
---  
8개 카테고리(정치, 경제, 사회, 생활/문화, 세계, 기술/IT, 연예, 스포츠)로 분류된 한국어 뉴스 기사를 대상으로 분류 모델을 구현한 프로젝트입니다. Mecab 형태소 분석기와 FastText 임베딩을 활용해 전처리 및 단어 벡터 모델을 구축하며, LSTM/CNN/Gru 등 5가지 딥러닝 모델의 성능을 비교 평가합니다. 최종적으로는 Yoon Kim의 CNN 기반 모델이 가장 높은 정확도를 달성한 텍스트 분류 솔루션입니다. 학습 데이터(0-159)와 테스트 데이터(160-199)로 구성된 1600개의 한국어 기사 데이터셋을 사용합니다.