---
Language: Dockerfile
tags:
 - Reverse Proxy
 - Nginx
 - Let's Encrypt
 - Docker
 - Self-Hosted
aliases:
 - NPM
 - Nginx Proxy Manager
 - 리버스 프록시 관리자
url: https://github.com/NginxProxyManager/nginx-proxy-manager/blob/develop/README.md
---
이 프로젝트는 Nginx와 Let's Encrypt를 기반으로 한 사용하기 쉬운 리버스 프록시 관리 도구입니다. Docker 컨테이너로 제공되어 복잡한 설정 없이도 SSL 인증서와 도메인 포워딩을 관리할 수 있으며, Tabler 기반의 직관적인 관리자 인터페이스가 특징입니다. 주로 가정에서 운영하는 웹 서비스나 자체 호스팅 환경에 적합하도록 설계되었습니다.  

주요 기능으로는 무료 SSL 인증서 발급, 접근 제어, 사용자 관리, 고급 Nginx 설정 등이 포함됩니다. 간단한 도커 컴포즈 설정으로 빠르게 시작할 수 있으며, 포트 포워딩과 도메인 설정만 완료하면 다른 웹 서비스들을 효율적으로 라우팅할 수 있습니다.