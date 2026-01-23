---
Language: Java  
tags:  
 - Spring Boot  
 - AWS  
 - Redis 캐싱  
 - Kafka ELK  
 - OAuth2 JWT  
aliases:  
 - MyCodeReview 백엔드  
 - 코드 리뷰 플랫폼 백엔드  
 - 코딩 테스트 정리 백엔드  
url: https://github.com/Seung-IL-Bang/MyCodeReview_backend  
---
코딩 테스트 문제 풀이를 정리·복습·공유할 수 있는 웹 사이트의 백엔드 시스템입니다. 7개월간 개인 프로젝트로 프론트엔드부터 백엔드, CI/CD까지 전 과정을 구현했으며, 성능 최적화(캐싱, 쿼리 개선), 확장성(오토 스케일링, DB 복제), 모니터링(Kafka+ELK) 등 다양한 기술을 적용했습니다. OAuth2·JWT 인증, QueryDSL 동적 쿼리, 낙관적 락을 통한 동시성 제어 등의 기능을 포함합니다.  

> 📌 **핵심 기술**: Spring Boot, AWS, Redis 캐싱, Kafka·ELK 스택, QueryDSL, OAuth2·JWT 인증  
> 📌 **주요 기능**: 게시글 관리, 댓글·답글, 좋아요, 리뷰 기능 및 성능 테스트용 더미 데이터 생성  
> 📌 **특화 분야**: DB 부하 분산, 무중단 배포, 실시간 로그 모니터링, N+1 문제 해결