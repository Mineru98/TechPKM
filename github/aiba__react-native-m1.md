---
Language: Ruby
tags:
 - React Native
 - Apple M1
 - Xcode
 - iOS
 - 환경설정
aliases:
 - React Native M1 설정
 - RN Apple Silicon
 - 리액트 네이티브 M1 빌드
url: https://github.com/aiba/react-native-m1/blob/main/README.md
---
Rosetta 없이 Apple M1(Apple Silicon) 환경에서 React Native 0.64.2 프로젝트를 정상적으로 컴파일하고 실행하는 방법을 단계별로 안내하는 가이드입니다. 캐시 삭제, Xcode 아키텍처 및 검색 경로 설정, 스위프트 브릿징 파일 생성, 그리고 Podfile 수정 및 의존성 재설치 과정을 포함하여 M1 칩셋 발생 빌드 오류를 해결하는 데 중점을 둡니다.