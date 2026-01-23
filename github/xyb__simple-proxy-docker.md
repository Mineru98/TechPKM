---
Language: Dockerfile
tags:
 - HTTP 프록시
 - Docker 컨테이너
 - 네트워크 구성
 - 오픈소스 활용
aliases:
 - simple-proxy-docker
 - 도커 기반 프록시 서버
url: https://github.com/xyb/simple-proxy-docker
---
이 프로젝트는 Docker로 실행할 수 있는 간단한 HTTP 프록시 서버를 제공합니다. jthomperoo의 simple-proxy를 기반으로 하며, 사전 빌드된 이미지 사용 또는 사용자 정의 이미지 빌드 두 가지 방식으로 운영 가능합니다. 기본 포트 8888에서 동작하며, 브라우저 또는 애플리케이션의 프록시 설정으로 활용할 수 있습니다.  

### 핵심 특징  
1. Docker 기반으로 간편한 배포 및 실행  
2. 사전 빌드 이미지 제공으로 즉시 사용 가능  
3. 기본 HTTP 프록시 기능 지원 (고급 기능 미지원)  
4. 사용자 정의 포트 및 설정 변경 가능  

### 사용 시나리오  
- 개발 환경 네트워크 테스트  
- 간단한 트래픽 라우팅 필요 시  
- Docker 기반 네트워크 구성 학습  

> ⚠️ 주의: 이 프록시는 기본적인 HTTP 요청만 처리하며, HTTPS 또는 고급 프록시 기능은 지원하지 않습니다.