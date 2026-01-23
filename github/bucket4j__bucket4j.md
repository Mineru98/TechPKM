---
Language: Java
tags:
 - rate-limiting
 - token-bucket
 - 분산 시스템
 - 동시성 제어
 - 스프링 부트
aliases:
 - 버킷4j
 - Bucket4j
 - 토큰 버킷
 - rate limiter
url: https://github.com/bucket4j/bucket4j
---
이 프로젝트는 Java 기반의 토큰 버킷 알고리즘을 활용한 속도 제한(rate-limiting) 라이브러리입니다. 정수 연산을 기반으로 한 정밀한 제어, 동시성 최적화, 클러스터링 환경 지원, 스프링 부트 통합 등 다양한 기능을 제공합니다. 8.16.0 버전은 Java 17 이상과 호환되며, Hazelcast, Redis, MongoDB 등 다양한 백엔드와 연동 가능합니다.

이 라이브러리는 고정밀도 계산, 동시성 제어, GC 친화적인 API, 모니터링 기능, 실시간 구성 변경 등의 핵심 기능을 갖추고 있으며, 특히 분산 시스템에서의 비동기 처리 지원을 강조합니다. 스프링 부트 스타터를 통해 간단한 설정으로 API 속도 제한을 구현할 수 있습니다.