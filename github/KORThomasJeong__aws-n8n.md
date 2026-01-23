---
Language: Bash
tags:
 - Docker
 - AWS Lightsail
 - 설치 스크립트
 - 자동화
 - Nginx Proxy Manager
aliases:
 - AWS Lightsail n8n 설치
 - n8n OpenWebUI 설치 가이드
 - Docker 자동화 스크립트
url: https://github.com/KORThomasJeong/aws-n8n
---
이 프로젝트는 AWS Lightsail 인스턴스에 n8n, Nginx Proxy Manager, OpenWebUI를 Docker로 한 번에 설치하는 자동화 스크립트를 제공합니다. Ubuntu 20.04 LTS 이상 환경에서 실행되며, 각 서비스는 별도 컨테이너로 관리되고 Nginx Proxy Manager를 통해 도메인 라우팅이 가능합니다. 설치 후 서비스별 설정 변경 및 관리 스크립트도 포함되어 있습니다.