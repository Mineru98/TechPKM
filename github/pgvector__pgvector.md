---
Language: C  
tags:  
 - 벡터 검색  
 - PostgreSQL  
 - 유사도 검색  
 - 오픈소스  
aliases:  
 - pgvector  
 - 벡터 유사도 검색  
 - PostgreSQL 벡터 확장  
url: https://github.com/pgvector/pgvector  
---
pgvector는 PostgreSQL을 위한 오픈소스 벡터 유사도 검색 확장입니다. 이 프로젝트는 Postgres의 기존 데이터와 함께 벡터를 저장하고, 정확한 및 근사 최근접 이웃 검색(Exact/Approximate Nearest Neighbor Search), 다양한 거리 계산 방법(L2, 코사인, 해밍 등), ACID 준수, JOIN 연산 등의 기능을 제공합니다. 단일/절반 정밀도, 이진 및 희소 벡터를 지원하며, HNSW 및 IVFFlat 인덱스를 통해 효율적인 검색 성능을 제공합니다. PostgreSQL 클라이언트 라이브러리가 있는 모든 언어와 호환됩니다.