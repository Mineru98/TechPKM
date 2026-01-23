---
Language: Python  
tags:  
 - 한국어-텍스트-분류  
 - 딥러닝-모델  
 - 형태소-분석  
 - FastText  
 - LSTM-GRU-CNN  
aliases:  
 - 한국어-뉴스-분류기  
 - Knews-classification  
 - 한국어-기사-카테고리화  
url: https://github.com/Moog303/Korean_News_Classification  
---
이 프로젝트는 8개 카테고리(정치, 경제, 사회 등)로 분류된 한국어 뉴스 기사를 딥러닝 모델로 분류하는 작업을 수행합니다. Mecab 형태소 분석기와 FastText 임베딩을 활용한 전처리 후, LSTM/GRU/CNN 기반 5가지 모델 성능을 비교 평가했습니다. Yoon Kim의 CNN 아키텍처가 최고 성능을 보였으며, 1,600개 기사 중 4:1 비율로 학습/테스트 셋을 구성해 검증되었습니다.