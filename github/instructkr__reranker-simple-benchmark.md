---
Language: Python  
tags:  
 - Reranker 벤치마크  
 - 한국어 검색 평가  
 - 정보 검색  
 - NLP  
 - BM25  
aliases:  
 - 한국어 리랭커 벤치마크  
 - Reranker 평가 프레임워크  
 - Korean Retrieval Benchmark  
url: https://github.com/instructkr/reranker-simple-benchmark  
---
본 프로젝트는 한국어 Reranker 모델을 평가하기 위한 경량화된 벤치마크 프레임워크로, BM25 기반 Stage 1 검색과 다양한 데이터셋(10개)을 활용한 Stage 2 리랭킹 평가를 제공합니다. Mecab 토크나이저와 Top-k 50 설정을 통해 효율적인 검색 성능을 분석하며, MRR/MAP/NDCG 등 다양한 지표로 모델 성능을 비교합니다. 주요 평가 대상 모델은 Qwen3-Reranker 시리즈와 BAAI/bge-reranker-v2-m3 등입니다.