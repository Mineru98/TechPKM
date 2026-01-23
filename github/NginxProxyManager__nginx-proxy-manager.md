---
Language: Dockerfile  
tags:  
 - Nginx  
 - Docker  
 - ReverseProxy  
 - SSL  
 - SelfHosting  
aliases:  
 - NginxProxyManager  
 - NPXM  
 - 리버스프록시관리  
url: https://github.com/NginxProxyManager/nginx-proxy-manager  
---
Nginx Proxy Manager는 Docker 이미지로 제공되는 프로젝트로, Nginx 및 Let's Encrypt 지식이 없는 사용자도 쉽게 리버스 프록시 및 SSL 종료를 설정할 수 있도록 설계되었습니다. 홈 네트워크 또는 다양한 환경에서 웹 서비스를 관리하는 데 특화되어 있으며, 사용자 친화적인 인터페이스를 통해 도메인 포워딩, 리다이렉션, 스트림 관리 등의 기능을 제공합니다. 무료 SSL 인증서 발급, 접근 제어, 고급 Nginx 설정 등 다양한 기능을 지원하며, 초보자부터 전문가까지 폭넓게 활용할 수 있습니다.  

주요 기술 스택은 Docker 기반의 Nginx와 Let's Encrypt이며, Tabler 기반 관리 인터페이스로 보안성과 사용 편의성을 동시에 확보했습니다. Docker Compose를 통한 간단한 설치와 포트 포워딩만으로 바로 사용할 수 있는 것이 특징입니다.