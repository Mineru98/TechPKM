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
 - Rust URL 쇼르텐러  
 - 딥링크 처리  
url: https://github.com/lee-lou2/url-shortener  
---  
Rust로 개발된 고성능 URL 단축 서비스입니다. 딥 링크 처리, 플랫폼별 리디렉션(iOS/Android), JWT 인증, 웹훅 알림 기능을 지원하며, PostgreSQL과 Redis를 활용한 효율적인 데이터 관리와 Base62 인코딩 기반의 충돌 없는 단축키 생성 시스템을 특징으로 합니다.  

이 프로젝트는 초당 요청 제한, 캐시 TTL 관리, 비동기 웹훅 처리 등 확장성 있는 아키텍처를 갖추고 있으며, Docker를 통한 배포와 환경 변수 기반의 유연한 설정 옵션을 제공합니다. MIT 라이선스로 배포됩니다.