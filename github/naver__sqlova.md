---
Language: Python  
tags:  
 - 자연어 처리  
 - SQL 생성  
 - 딥러닝  
 - BERT  
 - 신경망 시맨틱 파서  
aliases:  
 - SQLova  
 - 자연어-to-SQL  
 - 시맨틱 파서  
url: https://github.com/naver/sqlova  
---  
SQLova는 자연어 발화를 SQL 쿼리로 변환하는 신경망 시맨틱 파서입니다. Clova AI Research에서 개발되었으며, BERT 기반 임베딩과 시퀀스-to-SQL 모델링 기법을 결합하여 WikiSQL 데이터셋에서 83.6%의 논리적 정확도 및 89.6%의 실행 정확도를 달성했습니다. 이 프로젝트는 PyTorch와 BERT를 활용하며, 실행 가이드 디코딩을 적용한 SQLova-EG 모델도 포함되어 있습니다. 주요 특징으로는 테이블 인식 임베딩, 시퀀스-to-SQL 아키텍처, 실행 가이드 디코딩 기술이 있습니다.