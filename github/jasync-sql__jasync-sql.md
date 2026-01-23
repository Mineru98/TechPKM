---
Language: Kotlin  
tags:  
 - 비동기 데이터베이스 드라이버  
 - PostgreSQL  
 - MySQL  
 - Netty  
 - 코틀린  
aliases:  
 - jasync-sql  
 - 비동기 SQL 드라이버  
 - 코틀린 데이터베이스  
 - 넷티 기반 DB  
url: https://github.com/jasync-sql/jasync-sql  
---  
[jasync-sql](https://github.com/jasync-sql/jasync-sql)은 코틀린으로 작성된 단순하면서도 고성능의 비동기 데이터베이스 드라이버입니다. PostgreSQL과 MySQL을 지원하며, Netty 기반으로 구축되어 비차단(non-blocking) I/O를 통해 높은 처리 성능을 제공합니다.  

이 프로젝트는 더 이상 유지보수되지 않는 [mauricio/postgresql-async](https://github.com/mauricio/postgresql-async)를 포팅하여 개발되었으며, Scala 의존성을 제거함으로써 [Outbrain/ob1k](https://github.com/outbrain/ob1k) 등의 프로젝트에서 활용되고 있습니다.  

2.x 버전부터는 Java 8의 `java.time` API를 지원하며, R2DBC 확장 모듈, PostGIS 공간 데이터 타입 지원, Unix 도메인 소켓 연결 등의 기능을 포함합니다. 주요 사용처로는 Spring Data R2DBC, Vert.x, Quill 등이 있습니다.