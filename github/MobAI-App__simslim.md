---
Language: Go
tags:
 - iOS-Simulator
 - macOS
 - CI
 - 개발도구
 - 메모리-최적화
aliases:
 - SimSlim
 - simslim CLI
 - iOS 시뮬레이터 슬리밍
url: https://github.com/MobAI-App/simslim/blob/main/README.md
---
simslim은 macOS에서 iOS 시뮬레이터의 불필요한 백그라운드 데몬(Siri, Spotlight, iCloud 동기화 등)을 launchctl 비활성화로 꺼서 시뮬레이터당 메모리를 약 4배 절감해 주는 CLI 도구이자 Go 라이브러리입니다. 이를 통해 하나의 맥에서 실행 가능한 시뮬레이터 수를 크게 늘릴 수 있어, 개발·테스트·CI 및 AI 에이전트 기반 병렬 테스트 환경에 적합합니다. SwiftUI 기반 macOS 앱, JSON 프로파일, CI 사전 점검(doctor), 드리프트 검증(verify), 디스크 정리 기능도 제공합니다.