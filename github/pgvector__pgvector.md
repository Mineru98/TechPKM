---
Language: SQL
tags:
 - PostgreSQL
 - 벡터 검색
 - 유사도 검색
 - 확장 기능
 - AI 벡터
aliases:
 - pgvector
 - PostgreSQL 벡터 확장
url: https://github.com/pgvector/pgvector
---
pgvector는 PostgreSQL에 벡터 유사도 검색 기능을 제공하는 오픈소스 확장입니다. 벡터 데이터를 기존 데이터베이스와 통합하여 저장하고, 정확한/근사적인 최근접 이웃 검색(ANN)을 지원합니다. 다양한 거리 메트릭(L2, 코사인, 해밍 등)과 벡터 유형(실수, 반정밀도, 이진, 희소)을 지원하며, PostgreSQL의 ACID, 트랜잭션, JOIN 등 모든 고급 기능을 활용할 수 있습니다. Docker, Homebrew, PGXN 등 다양한 설치 방법을 제공합니다.