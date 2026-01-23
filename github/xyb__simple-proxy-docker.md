---
Language: Dockerfile  
tags:  
 - HTTP 프록시  
 - Docker  
 - 네트워크 프록시  
 - 컨테이너  
 - 간단한 프록시 서버  
aliases:  
 - simple-proxy-docker  
 - 간단한 프록시 도커  
 - xyb-simple-proxy  
url: https://github.com/xyb/simple-proxy-docker  
---
이 프로젝트는 도커를 사용하여 실행할 수 있는 간단한 HTTP 프록시 서버입니다. jthomperoo의 simple-proxy 오픈소스 프로젝트를 기반으로 하며, 사전 빌드된 도커 이미지 사용 또는 직접 빌드 후 실행 방법을 제공합니다. 기본적으로 8888 포트를 사용하며, 클라이언트는 이 포트를 통해 프록시 설정을 구성할 수 있습니다.  

## 핵심 기능  
- Docker를 통한 간편한 배포 및 실행  
- HTTP 프록시 기능 제공  
- 기본 포트 8888 사용 (변경 가능)  
- curl 명령어로 프록시 작동 확인 가능  

## 주요 명령어  
- **사전 빌드 이미지 실행**: `docker run -d -p 8888:8888 xieyanbo/simple-proxy`  
- **컨테이너 정지**: `docker stop $(docker ps -q --filter ancestor=simple-proxy)`  

> 참고: 이 프록시는 기본적인 HTTP 프록시 기능만 제공하며, 고급 프록시 서버의 모든 기능을 지원하지 않습니다.