---
Language: Python
tags:
 - PII 가명화
 - 한국어 NLP
 - RAG 전처리
 - 개인정보보호
 - 규칙 기반 검출
aliases:
 - ko-pii
 - 한국어 PII 검출기
 - 한국어 개인정보 마스킹
url: https://github.com/Marker-Inc-Korea/ko-pii/blob/main/README.md
---
외부 ML 의존성 없이 규칙, 사전, 체크섬만으로 한국어 문서의 개인정보를 검출하고 가역적으로 가명화하는 Python 라이브러리입니다. 공공 문서 및 RAG 파이프라인의 전처리 레이어로 활용하기 최적화되어 있으며, 33개의 한국 특화 PII 카테고리를 지원하고 복원 기능(Vault)과 결합 위험도 평가를 제공합니다.