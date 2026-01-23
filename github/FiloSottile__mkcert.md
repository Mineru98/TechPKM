---
Language: Go
tags:
 - 개발 인증서 생성
 - 로컬 개발 환경
 - TLS 인증서
 - 자동화된 CA 설정
 - 크로스플랫폼
aliases:
 - mkcert
 - 로컬 개발 인증서
 - 로컬 CA 생성기
url: https://github.com/FiloSottile/mkcert
---
mkcert는 로컬 개발 환경에서 신뢰할 수 있는 테스트 인증서를 쉽게 생성하는 도구입니다. 실제 인증서 기관(CA) 대신 자체 서명된 인증서의 신뢰 문제를 해결하기 위해 시스템 신뢰 저장소에 로컬 CA를 자동 설치합니다. 다양한 플랫폼(macOS, Linux, Windows)과 브라우저(Firefox, Chrome 등)를 지원하며, 여러 호스트 이름(예: `localhost`, `127.0.0.1`, 사용자 정의 도메인)에 대한 인증서를 생성할 수 있습니다. 개발 환경에서 TLS/SSL 테스트 시 편리하며, 복잡한 설정 없이 단일 명령어로 인증서를 발급합니다.