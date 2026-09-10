---
Language: C
tags:
 - PostgreSQL
 - FullTextSearch
 - BM25
 - 검색엔진
 - 데이터베이스
aliases:
 - pg_textsearch
 - Tapir
 - PostgreSQL BM25 검색
url: https://github.com/timescale/pg_textsearch
---
pg_textsearch는 PostgreSQL 17/18을 위한 최신 랭킹 기반 텍스트 검색 확장으로, BM25 스코어링과 간단한 `ORDER BY content <@> '검색어'` 문법을 통해 관련도 순 문서 검색을 제공한다. Block-Max WAND 최적화, 표현식/부분 인덱스, 다국어 지원, 병렬 인덱스 빌드 등을 갖추어 프로덕션 수준의 성능과 확장성을 목표로 하며, Timescale에서 개발하고 있다(초기 프로젝트 이름은 Tapir였다).