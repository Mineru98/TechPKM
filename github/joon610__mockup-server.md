---
Language: JavaScript
tags:
 - mock-api-server
 - 프론트엔드 개발
 - mock-server
 - 전자 애플리케이션
 - JSON 관리
aliases:
 - mock-up-server
 - mock-server-electron
 - 프론트엔드 백엔드 동기화
- 가상 API 서버
url: https://github.com/joon610/mockup-server
---
이 프로젝트는 프론트엔드와 백엔드 개발 중 서버 없이 개발할 때 발생하는 문제(비동기 처리, 변수명, 객체 타입, API 설계 등)를 줄이기 위한 가상 API 서버입니다. JSON 파일 기반의 간단한 설정으로 CRUD(Create, Read, Update, Delete) 기능을 제공하며, GitHub을 통한 협업과 Git 기반 관리가 가능합니다. Electron 기반의 데스크톱 애플리케이션으로 Windows와 Mac 환경에서 실행됩니다.  

핵심 기능은 디렉터리 구조 기반의 API 경로 설정, 응답 데이터 관리(index.json), 헤더/쿠키 설정(setting.json), 요청 로그 기록(requestLog.json) 등을 지원합니다. MIT 라이선스로 배포되어 자유롭게 사용할 수 있습니다.