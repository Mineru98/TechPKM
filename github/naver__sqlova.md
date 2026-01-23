---
Language: Python  
tags:  
 - 자연어 처리  
 - SQL 생성  
 - 딥러닝  
 - BERT  
 - 신경망 의미 분석  
aliases:  
 - SQLova  
 - 검색 및 클로바  
 - 자연어-SQL 변환  
 - 신경망 의미 파서  
url: https://github.com/naver/sqlova/blob/master/README.md  
---
SQLova는 자연어 문장을 SQL 쿼리로 변환하는 신경망 기반 의미 파서입니다. 네이버 클로바 AI 연구팀이 개발했으며, BERT 기반 임베딩과 실행 가이드 디코딩 기술을 활용하여 WikiSQL 데이터셋에서 83.6%의 논리 형식 정확도를 달성했습니다. SQLNet 아키텍처를 개선한 이 모델은 테이블 구조와 문맥을 고려한 SQL 생성 기능을 제공합니다. PyTorch 0.4.0 이상과 CUDA 9.0 환경에서 실행 가능하며, Apache 2.0 라이선스로 배포됩니다.