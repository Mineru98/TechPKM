---
Language: Python  
tags:  
 - 한국어 토크나이저  
 - 재랭킹 벤치마킹  
 - 정보 검색  
 - MTEB 데이터셋  
 - 경량화 평가  
aliases:  
 - Make Reranker Benchmark Simple  
 - Reranker 벤치마크 경량화  
 - 한국어 검색 평가 시스템  
url: https://github.com/instructkr/retriever-simple-benchmark  
---  
본 프로젝트는 한국어 재랭킹 모델 평가를 위한 벤치마킹 시스템으로, BM25 기반 검색 후 상위 50개 문서를 재랭킹하는 2단계 프로세스를 경량화하여 구현했습니다. 10개의 한국어 벤치마크 데이터셋(총 18,945개 쿼리)을 지원하며, Mecab 토크나이저와 다양한 재랭킹 모델(Qwen3, bge 등)의 성능 비교를 제공합니다. 최소 의존성 환경에서 빠른 실행과 즉각적인 결과 분석이 가능하도록 설계되었습니다.