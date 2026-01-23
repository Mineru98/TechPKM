---
Language: Python  
tags:  
 - 한국어 처리  
 - 텍스트 전처리  
 - 딥러닝 NLP  
 - 자연어 처리  
 - KoSpacing  
aliases:  
 - PyKoSpacing  
 - 한국어서토큰화  
 - 한국어띄어쓰기  
url: https://github.com/haven-jeon/PyKoSpacing  
---  
PyKoSpacing은 한국어 텍스트의 자동 띄어쓰기 처리를 위한 Python 패키지입니다. 딥러닝 모델 기반(1억 개 이상의 뉴스 기사 학습)으로 SNS/SMS 텍스트에 특화된 97% 이상의 정확도를 제공하며, 복합어 정규화 시 성능 향상이 가능합니다. 사용자는 규칙 기반 예외 처리 또는 CSV 파일을 통해 맞춤형 띄어쓰기를 설정할 수 있으며, 영어 문자 처리 시 `ignore` 파라미터로 유연한 대응이 가능합니다.  

핵심 기능:  
1. 딥러닝 기반 자동 띄어쓰기  
2. 규칙 기반 예외 처리  
3. 영어/기호 혼합 텍스트 처리  
4. CLI 및 Python API 지원