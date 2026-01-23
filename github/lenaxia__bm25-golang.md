---
Language: Go
tags:
 - BM25
 - 검색엔진
 - 정보검색
 - Golang 구현
 - 랭킹 알고리즘
aliases:
 - BM25 Golang
 - BM25 구현체
 - 검색 랭킹 알고리즘
url: https://github.com/lenaxia/bm25-golang
---
이 프로젝트는 Go 언어로 구현된 다양한 BM25 변형 알고리즘(Okapi BM25, BM25L, BM25+, BM25-Adpt, BM25T)을 제공합니다. 검색 엔진에서 문서와 검색 쿼리의 관련성을 추정하는 랭킹 함수로, 대량의 문서 처리 시 병렬 및 배치 연산을 지원하여 성능을 최적화했습니다. 토큰화 기능과 함께 문서 집합(Corpus)을 기반으로 관련성 점수 계산 및 상위 문서 추출이 가능합니다.  

연구 논문 ["A Study of Efficient and Robust IR Metrics"](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.723.8440&rep=rep1&type=pdf)을 기반으로 구현되었으며, Python 기반 BM25 라이브러리(rank_bm25)에서 영감을 받았습니다.