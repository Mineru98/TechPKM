---
Language: SQL
tags:
 - snowflake
 - id-generator
 - mysql
 - auto-increment
 - distributed-system
aliases:
 - 스노플레이크 MySQL
 - 분산 ID 생성기
 - 스노플레이크 ID 생성
url: https://github.com/yejianfei/snowflake-mysql
---
이 프로젝트는 MySQL 환경에서 분산 시스템의 ID 생성을 위한 Twitter Snowflake 알고리즘을 구현한 솔루션입니다. 글로벌 자동 증가 테이블을 생성하여 데이터베이스 수준 ID 생성기를 제공하며, 여러 데이터베이스에서 사용 시 노드 설정 변경이 필요합니다. `REPLACE INTO` 문을 사용하므로 다른 테이블에서 `AUTO_INCREMENT`를 사용할 수 없습니다.  

사용 방법: `tb_tickets.sql`로 테이블 생성 후 `gen_ticket64.sql`로 함수를 생성하고, `SELECT gen_ticket64()`로 ID를 조회합니다. 에포크 시작일과 노드 ID는 `gen_ticket64.sql`에서 수정 가능합니다.