---
Language: Python
tags:
 - Text-to-SQL
 - 한국어 처리
 - 딥러닝 모델
 - 위키SQL
 - 자연어 처리
aliases:
 - SPARTA
 - 한국어-SQL 변환
 - Text2SQL
 - 한국어 질의 변환
 - Korean-SQL
url: https://github.com/TooTouch/SPARTA
---
SPARTA는 한국어 텍스트를 SQL 쿼리로 변환하는 딥러닝 모델을 구현한 프로젝트입니다. 고려대학교 DSBA 연구실의 '비정형 텍스트 분석' 수업에서 진행된 팀 프로젝트로, 영어 WikiSQL 데이터셋을 한국어로 번역하여 다양한 방법으로 학습된 모델을 평가했습니다. SQLova, HydraNet, BRIDGE 등의 모델을 활용하며, 논리적 정확성(65.8%)과 실행 정확성(74.3%)을 달성했습니다. 4가지 번역 전략(Where+Select, Where, Table+Header, Table)을 적용한 데이터셋과 사전 훈련된 모델을 제공합니다.