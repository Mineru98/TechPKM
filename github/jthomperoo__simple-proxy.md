---
Language: Go
tags:
 - HTTP/HTTPS 프록시
 - 네트워크 도구
 - GoLang
 - 로깅 시스템
 - SOCKS5 터널링
aliases:
 - simple-proxy
 - 간단한 프록시 서버
 - HTTP 프록시 바이너리
 - self-contained proxy
url: https://github.com/jthomperoo/simple-proxy
---
이 프로젝트는 독립적인 바이너리로 배포되는 간단한 HTTP/HTTPS 프록시 서버입니다. 지정된 포트에서 실행되며 인증, 로깅, SOCKS5 프록시 터널링 등의 기능을 지원합니다. `glog`를 기반으로 한 로그 옵션과 기본 인증 기능을 통해 유연한 설정이 가능하며, 다양한 운영체제에서 직접 실행할 수 있는 경량 도구로 설계되었습니다.  

주요 특징으로는 로그 레벨 조정, 인증서/키 파일 지정, 요청 헤더 로깅, 프록시 성능 테스트 기능 등이 포함됩니다.