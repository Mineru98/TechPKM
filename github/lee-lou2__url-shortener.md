---
Language: Rust
tags:
 - URL 단축 서비스
 - Axum
 - PostgreSQL
 - Redis
 - JWT 인증
aliases:
 - URL 단축기
 - url-shortener
 - 딥링크 처리
url: https://github.com/lee-lou2/url-shortener
---
Rust 기반 고성능 URL 단축 서비스로, 딥 링크 처리, 플랫폼별 리디렉션, JWT 인증, 웹훅 알림 기능을 제공합니다. Axum 웹 프레임워크와 PostgreSQL/Redis 저장소를 사용하며, Base62 인코딩과 xxHash를 활용해 효율적인 단축키 생성과 중복 URL 관리를 구현했습니다. 캐싱 전략으로 Redis와 MessagePack을 사용하여 빠른 응답과 리소스 효율성을 확보했습니다.