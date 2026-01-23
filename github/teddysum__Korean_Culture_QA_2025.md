---
Language: Python
tags:
 - 한국어-문화-QA
 - 모델-평가
 - NLP
 - 국립국어원
 - 베이스라인
aliases:
 - 한국문화-질의응답-베이스라인
 - AI말평-한국문화-QA
 - Korean-Culture-QA-Baseline
url: https://github.com/teddysum/korean_evaluation.git
---
본 프로젝트는 국립국어원 주최 '2025년 인공지능의 한국어 능력 평가' 경진대회 중 '한국문화 질의응답' 과제에 대한 베이스라인 모델 평가 및 재현 코드를 제공합니다. Qwen3-8B와 HyperCLOVAX Text 1.5B 모델의 성능을 Accuracy, EM, ROUGE, BERTScore 등 다양한 지표로 분석하며, JSON 형식의 문화 지식 QA 데이터셋 처리와 추론 실행 스크립트를 포함합니다.  

선다형/단답형/서술형 문제 유형별 평가 체계를 구현하고 있으며, Bllossom/llama-3.2-Korean-Bllossom-3B 등의 한국어 모델 호환 추론을 지원합니다. 평가 코드와 샘플 데이터를 포함해 재현성을 확보한 점이 특징입니다.