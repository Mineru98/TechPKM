---
Language: Python, Rust
tags:
 - Information Retrieval
 - BM25
 - Hybrid Search
 - Bayesian Calibration
 - RAG
aliases:
 - Bayesian BM25
 - bb25
url: https://github.com/instructkr/bb25
---
BM25 알고리즘에 베이지안 보정(Bayesian Calibration)을 적용하여 하이브리드 검색 성능을 개선한 `bb25` 프로젝트입니다. 벡터 검색(Dense)과의 결합 시 스케일 불일치 문제를 완화하여, 기존 방식보다 높은 NDCG 및 MRR 점수를 달성하는 것이 특징입니다. Python과 Rust로 구현되었으며, 단순한 API와 실험 도구를 포함하여 자체 포함된 방식으로 동작합니다.