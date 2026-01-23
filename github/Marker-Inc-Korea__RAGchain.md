---
Language: Python
tags:
 - RAG
 - LLM
 - 자연어처리
 - 정보검색
 - 문서분석
aliases:
 - RAG체인
 - RAG프레임워크
 - RAG워크플로우
 - RAGchain
url: https://github.com/Marker-Inc-Korea/RAGchain
---
RAGchain은 LLM 기반 고급 RAG(검색 증강 생성) 워크플로우 개발을 위한 프레임워크입니다. 기존 Langchain 등의 도구보다 복잡한 RAG 파이프라인 구축과 높은 정확도 구현이 용이하며, OCR 로더, 다중 검색기 지원, 사전 제작 파이프라인 등의 고급 기능을 제공합니다. Langchain과의 부분적 호환성을 통해 다양한 통합 기능을 활용할 수 있습니다.

핵심 기술 스택으로 BM25, 벡터 DB, Hybrid 검색 방식을 지원하며, OCR 모델(Nougat, Deepdoctection)과 재정렬기(UPR, TART, MonoT5 등)를 통한 정확도 향상 기능을 포함합니다. 벤치마크 모듈과 다양한 데이터셋(MS-MARCO, TriviaQA 등) 평가를 지원하여 RAG 시스템 성능 검증이 가능합니다.