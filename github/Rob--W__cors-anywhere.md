---
Language: JavaScript
tags:
 - NodeJS
 - CORS 프록시
 - 서버 설정
 - API 게이트웨이
 - 보안 헤더
aliases:
 - CORS Anywhere
 - cors-anywhere
 - CORS 프록시 서버
url: https://github.com/Rob--W/cors-anywhere
---
CORS Anywhere는 NodeJS 기반의 프록시 서버로, 타겟 요청에 CORS 헤더를 추가하여 크로스-도메인 요청을 가능하게 합니다. 프록시할 URL은 경로에서 직접 추출되며, 프로토콜 생략 시 기본적으로 HTTP를 사용하고 포트 443 지정 시 HTTPS로 자동 전환됩니다. 사용자 인증 요청은 차단되며, 프록시 요청 시 특정 헤더 요구사항을 설정하여 브라우저의 직접 접근을 방지할 수 있습니다. Heroku 등 클라우드 환경에서의 배포를 지원하며, 요청 필터링/헤더 조작/속도 제한 등의 보안 기능을 제공합니다.