---
Language: Java/Kotlin
tags:
 - Spring Test
 - Transactional Alternative
 - Test Data Management
 - JUnit Extension
 - Integration Testing
aliases:
 - no-transactional
 - 트랜잭션 없는 테스트
 - @Transactional 대체
 - 테스트 데이터 초기화
url: https://github.com/banlife/no-transactional
---
Spring Framework에서 제공하는 `@Transactional` 어노테이션을 사용하지 않고 테스트하고자 할 때 유용한 테스트 지원 라이브러리입니다. 각 테스트 실행 전 데이터를 자동 초기화하고, `@Transactional` 사용 시 테스트를 강제 중단하여 트랜잭션 없는 테스트 환경을 보장합니다. JUnit 5 확장 모델과 호환되며, `@DataJpaTest` 등 내부적으로 트랜잭션을 사용하는 테스트도 감지합니다.  

> 🚀 Jitpack을 통해 배포되며, 테스트 코드에서 데이터베이스 트랜잭션 이슈를 회피하는 데 특화된 도구입니다.