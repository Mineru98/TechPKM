---
Language: Python  
tags:  
 - RAG  
 - LLM  
 - 도메인 적응  
 - 검색 증강 생성  
 - 파인튜닝  
aliases:  
 - DALM  
 - Domain Adapted Language Model Toolkit  
 - Arcee DALM  
 - RAG-엔드투엔드  
url: https://github.com/arcee-ai/DALM  
---  
Arcee에서 오픈소스로 공개한 DALM 툴킷은 특정 도메인에 맞춰 언어 모델을 적응시키는 도구로, 검색 증강 생성(RAG) 아키텍처와 디코더 전용 언어 모델(Llama, Falcon 등)의 통합 훈련을 지원합니다. 이 프로젝트는 특허, 의학 논문, 금융 보고서 등 특정 분야의 데이터로 LLM을 미세 조정해 전문성과 정확성을 높이는 것을 목표로 합니다. Hugging Face 모델과 호환되며, 대조 학습과 엔드투엔드 훈련 방식을 통해 효율적인 도메인 적응이 가능합니다.  

핵심 기능으로는 검색기 단독 훈련, 검색기-생성기 통합 훈련(RAG-e2e), 그리고 평가 스크립트가 포함되어 있습니다. CSV 형식의 데이터셋(지문, 쿼리, 답변)을 사용하며, BAAI/bge-large-en 검색기와 Llama-2-7b-hf 생성기를 기본 모델로 지원합니다. 성능 측정 지표로는 재현율(recall)과 히트율(hit rate)을 활용합니다.