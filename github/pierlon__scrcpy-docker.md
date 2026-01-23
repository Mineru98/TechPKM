---
Language: Dockerfile
tags:
 - Docker
 - Android
 - 원격제어
 - scrcpy
 - GPU지원
aliases:
 - scrcpy-docker
 - 안드로이드-원격제어
 - 도커-스크린미러링
url: https://hub.docker.com/r/pierlo1/scrcpy/
---
scrcpy는 안드로이드 기기를 원격으로 제어할 수 있는 오픈소스 프로젝트를 도커 이미지로 제공하는 배포판입니다. AMD, Intel, Nvidia GPU 아키텍처에 최적화된 별도 이미지를 지원하며, USB 연결 장치를 통해 실시간으로 기기 화면을 미러링하고 제어할 수 있습니다. 컨테이너 환경에서 adb(Android Debug Bridge)와 연동해 동작하며, Docker Compose도 지원합니다.  

이 프로젝트는 개발자/테스터가 호스트 머신에서 별도의 adb 서버 설치 없이 컨테이너로 안드로이드 디버깅 환경을 구성할 수 있도록 설계되었습니다. X11 서버 통합을 통해 그래픽 출력도 지원합니다.