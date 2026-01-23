---
Language: Java/Kotlin
tags:
 - Spring Transaction
 - 테스트 유틸리티
 - @Transactional 대체
 - JPA 테스트
 - 테스트 데이터 초기화
aliases:
 - no-transactional
 - 트랜잭션 없는 테스트
 - @Transactional 강제 중단
url: https://github.com/banlife/no-transactional
---
**no-transactional**은 Spring Framework의 `@Transactional` 어노테이션을 사용하지 않고 테스트 데이터 초기화를 수행하는 테스트 유틸리티 라이브러리입니다. 테스트 클래스/메서드에서 `@Transactional` 사용을 강제로 차단하며, `@DataJpaTest`와 같은 내장 트랜잭션 어노테이션도 감지합니다. JPA 기반 프로젝트에서 테스트 환경에 대한 통제력을 높이도록 설계되었습니다.  

> 요약: 트랜잭션 없이 테스트 데이터 관리를 지원하는 Spring 테스트 유틸리티 모듈로, 기존 `@Transactional` 의존성을 제거합니다.