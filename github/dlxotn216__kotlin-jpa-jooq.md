---
Language: Kotlin
tags:
 - Kotlin
 - Spring Boot
 - JPA
 - jOOQ
 - DB접근계층
aliases:
 - Kotlin JPA jOOQ 혼합 사용
 - jOOQ CUD 프로토타입
 - jOOQ Hibernate 하이브리드 아키텍처
url: https://github.com/dlxotn216/kotlin-jpa-jooq/blob/master/README.md
---
데이터 저장은 JPA를, 복잡한 쿼리와 페이지네이션은 jOOQ를 사용하는 하이브리드 아키텍처를 실험하는 Kotlin/Spring Boot 프로젝트입니다. jOOQ 단독 사용 시 발생하는 Entity-Record 변환의 번거로움, Schema 관리 이슈, SQL 중심적 사고방식의 한계를 실제 비즈니스 로직 구현을 통해 분석하고 검증합니다. 결론적으로 CUD는 JPA를, 복잡한 조회는 jOOQ를 사용하는 방식이 가장 합리적임을 도출하며, 테스트 환경에서는 TestContainer 활용을 제안합니다.