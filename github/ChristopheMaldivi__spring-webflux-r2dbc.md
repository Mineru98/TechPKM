---
Language: Java
tags:
 - Spring-WebFlux
 - R2DBC
 - Reactive-Programming
 - PostgreSQL
 - REST-API
aliases:
 - Spring WebFlux R2DBC 예제
 - 스프링 리액티브 비동기 DB 연동
url: https://github.com/ChristopheMaldivi/spring-webflux-r2dbc/blob/main/README.MD
---
외부 국가 정보 REST API를 WebClient로 호출하고, R2DBC를 활용하여 PostgreSQL에 비동기 방식으로 데이터를 저장하는 Spring WebFlux 기반의 간단한 예제 프로젝트입니다. 전통적인 @Async 방식 대신 Reactor의 Mono와 Flux API를 기반으로 한 리액티브 스택의 비동기 처리 방식을 적용하였습니다.