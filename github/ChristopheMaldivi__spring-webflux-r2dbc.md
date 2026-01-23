---
Language: Java
tags:
 - Spring Webflux
 - R2DBC
 - Reactor
 - 비동기 프로그래밍
 - PostgreSQL
aliases:
 - 스프링 웹플럭스 예제
 - 국가 정보 조회 시스템
 - 리액터 모노/플럭스
url: https://github.com/example/spring-webflux-country-demo
---
이 프로젝트는 Spring Webflux와 R2DBC를 사용하여 국가 정보를 비동기적으로 조회하고 저장하는 간단한 사용 사례를 구현한 것입니다. REST API에서 국가 데이터를 가져온 후 PostgreSQL에 비동기적으로 저장하며, Reactor의 Mono/Flux를 기반으로 동작합니다. 서버 실행 후 curl 명령어로 API 테스트 가능하며, 비동기 스택의 장점을 보여주는 예제입니다. MIT 라이선스로 배포됩니다.