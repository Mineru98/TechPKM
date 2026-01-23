---
Language: Python
tags:
 - Fixed-Dimensional-Encoding
 - ColBERT
 - Multi-vector-retrieval
 - Information-Retrieval
 - Similarity-Search
aliases:
 - MUVERA
 - FDE
 - Multi-Vector-Embedding
 - 고정차원인코딩
url: https://github.com/google/graph-mining/tree/main/sketching/point_cloud
---
이 프로젝트는 ColBERT 스타일의 다중 벡터 표현을 효율적으로 검색하기 위한 고정차원인코딩(FDE) 알고리즘을 Python으로 구현한 것입니다. 원본 C++ 구현과 동일한 동작을 보장하면서 접근성을 높였으며, 대규모 문서에서 벡터 간 유사도 관계를 유지하면서 단일 고정 차원 벡터로 변환하는 기능을 제공합니다. 검색 시스템에서의 정확성과 속도를 동시에 개선하는 것이 주요 목적입니다.