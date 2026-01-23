---
Language: Dockerfile  
tags:  
 - 안드로이드_에뮬레이터  
 - 도커_이미지  
 - 모바일_테스트  
 - CI_CD  
 - 앱_개발  
aliases:  
 - docker-android  
 - 안드로이드_도커  
 - 모바일_테스트_환경  
 - Genymotion_통합  
url: https://github.com/budtmo/docker-android  
---  
이 프로젝트는 Android 애플리케이션 개발 및 테스트를 위한 도커 이미지를 제공합니다. 다양한 Android 버전과 디바이스 프로필을 지원하며, VNC를 통한 컨테이너 시각화, 로그 공유, ADB 연결 등 다양한 기능을 포함합니다. Genymotion과의 통합 및 클라우드 솔루션과의 호환성을 통해 테스트 및 개발 환경을 효율적으로 구성할 수 있습니다.  

주요 특징:  
1. Samsung Galaxy, Nexus 시리즈 등 다양한 디바이스 프로필 지원  
2. 컨테이너 외부에서 ADB로 에뮬레이터 제어 가능  
3. Appium, Espresso 등 테스트 프레임워크와 호환  
4. WSL2 환경에서 하드웨어 가속 지원 (Windows 11 전용)  
5. 데이터 지속성을 위한 볼륨 마운트 기능 제공  

프로 버전에서는 프록시 설정, 언어 변경, 헤드리스 모드 등 추가 기능 제공(활성 스폰서 대상)