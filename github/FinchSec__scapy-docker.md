---
Language: Dockerfile
tags:
 - 네트워크
 - 보안
 - 패킷 분석
 - 컨테이너
 - Scapy
aliases:
 - Scapy Docker
 - 패킷 분석 컨테이너
 - FinchSec Scapy
url: https://hub.docker.com/r/finchsec/scapy
---
이 프로젝트는 네트워크 패킷 분석을 위한 Python 기반 도구인 Scapy를 Docker 컨테이너로 제공하는 것을 목적으로 합니다. 매일 자동으로 빌드되어 업데이트되며, 네트워크 보안 분석 및 패킷 조작용 컨테이너 환경으로 활용 가능합니다. 특권한 모드(`--privileged`)와 호스트 네트워크(`--net=host`)에서 실행하여 실제 네트워크 인터페이스를 직접 접근할 수 있도록 설계되었습니다. DockerHub에서 간편하게 가져와 실행할 수 있는 인프라를 제공합니다.