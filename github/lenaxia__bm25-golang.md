---
Language: Go  
tags:  
 - 검색엔진  
 - 정보검색  
 - 랭킹함수  
 - BM25  
 - 병렬처리  
aliases:  
 - BM25 구현  
 - BM25 Go  
 - Okapi BM25  
 - Go 검색 알고리즘  
url: https://github.com/lenaxia/bm25-golang  
---  
이 프로젝트는 Go 언어로 구현된 다양한 BM25 변형 알고리즘(Okapi BM25, BM25L, BM25+, BM25-Adpt, BM25T)을 제공합니다. 검색 엔진에서 문서와 쿼리의 관련성을 평가하는 랭킹 함수로 사용되며, 대규모 코퍼스와 병렬 처리를 지원하는 것이 특징입니다. Python 구현체에서 영감을 받아 Go의 동시성 기능을 활용하여 성능을 최적화했습니다.