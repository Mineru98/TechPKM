---
Language: SQL
tags:
 - Snowflake
 - ID 생성기
 - MySQL
 - 분산 시스템
 - 자동 증가
aliases:
 - snowflake-mysql
 - 분산 ID 생성
 - MySQL Snowflake
url: https://github.com/yejianfei/snowflake-m9aster/README.md
---
이 프로젝트는 MySQL에서 트위터의 Snowflake 알고리즘을 구현한 ID 생성기입니다. 데이터베이스 수준에서 글로벌 고유 ID를 생성하기 위한 자동 증가 테이블과 함수를 제공합니다. `REPLACE INTO`를 사용해 중복 방지 기능을 구현했으며, 여러 데이터베이스 환경에서 노드 ID를 변경해 독립적으로 사용할 수 있습니다. `gen_ticket64()` 함수로 Snowflake ID를 생성할 수 있습니다.