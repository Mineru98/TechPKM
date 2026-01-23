---
Language: JavaScript
tags:
 - NodeJS 프록시
 - CORS 헤더
 - 서버 설정
 - API 프록시
 - 보안 헤더
aliases:
 - cors-anywhere
 - CORS 프록시 서버
 - CORS 우회 서버
url: https://github.com/Rob--W/cors-anywhere
---
CORS Anywhere는 NodeJS 기반의 프록시 서버로, 요청된 URL에 CORS 헤더를 추가하여 브라우저의 크로스-도메인 요청 제한을 해결합니다. 클라이언트는 대상 URL을 프록시 경로로 전달하여 CORS 정책 없이 안전하게 데이터를 요청할 수 있으며, 서버는 화이트리스트, 블랙리스트, 헤더 필터링 등의 보안 설정을 지원합니다. 헤로쿠 배포 및 자체 호스팅이 가능한 오픈소스 프로젝트입니다.