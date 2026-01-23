---
Language: Java
tags:
 - rate-limiting
 - token-bucket
 - 분산시스템
 - SpringBoot
 - 동시성제어
aliases:
 - 버킷4j
 - 토큰버킷
 - rate-limiting 라이브러리
 - Bucket4j
url: https://github.com/bucket4j/bucket4j
---
Bucket4j는 토큰 버킷 알고리즘을 기반으로 한 Java용 레이트 리미팅 라이브러리입니다. 단일 JVM 또는 클러스터된 환경에서 정확한 정수 연산을 통해 레이트 리미팅을 구현하며, 동시성 처리와 다양한 백엔드(인메모리, JCache, Hazelcast, Redis, MongoDB, JDBC 등)를 지원합니다. Spring Boot Starter를 통해 설정 기반 통합이 가능하며, 로컬 캐싱 솔루션과의 연동도 제공합니다.  

주요 기능으로는 무부동 소수점 연산, 비동기 API, 구성 변경 가능성, 모니터링용 리스너 API 등이 포함됩니다. 동시성 전략 선택과 가비지 컬렉션 최적화도 특징입니다.