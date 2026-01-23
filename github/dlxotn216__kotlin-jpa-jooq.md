---
Language: Kotlin  
tags:  
 - JOOQ  
 - JPA  
 - Spring Boot  
 - MariaDB  
 - Entity 관리  
aliases:  
 - Kotlin-JOOQ-JPA-SpringBoot  
 - 데이터베이스쿼리관리  
 - 멀티ORM통합  
url: https://github.com/dlxotn216/jooq-jpa-multi-orm  
---
이 프로젝트는 Kotlin 환경에서 JOOQ와 JPA를 혼용해 복잡한 쿼리와 데이터 관리를 동시에 처리하는 아키텍처를 탐구합니다. JPA로 기본 엔티티 관리를 수행하면서 JOOQ를 활용해 페이지네이션 및 복잡한 SQL 연산을 수행하며, Docker를 통한 MariaDB 환경에서 실제 운영 DB와 유사한 테스트 환경을 구축하는 방법을 실험합니다. 주요 이슈는 JOOQ의 코드 생성 스크립트 관리, DBMS 종속성 문제, 그리고 엔티티 변경 감지 로직의 구현에 초점을 맞춥니다. Mockito를 활용한 테스트 기법과 JPA의 연관 엔티티 관리 최적화 사례도 포함되어 있습니다.