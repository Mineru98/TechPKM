---
Language: Go
tags:
 - 시스템 모니터링
 - Wails
 - React
 - TypeScript
 - 크로스플랫폼
aliases:
 - 시스템 모니터링 대시보드
 - HWnow
 - 실시간 리소스 모니터링
url: https://github.com/hong-seongmin/HWnow
---
HWnow는 Go + React + TypeScript + Wails v2로 개발된 크로스플랫폼 네이티브 데스크톱 애플리케이션입니다. CPU, 메모리, 디스크, 네트워크, GPU 등 시스템 리소스를 3초 간격으로 실시간 모니터링하며, 드래그 앤 드롭으로 위젯을 자유롭게 배치/조정할 수 있는 사용자 정의 가능한 대시보드를 제공합니다. 라이트/다크 테마 지원과 반응형 디자인으로 다양한 환경에서 사용 가능하며, NVIDIA GPU 모니터링과 프로세스 관리 기능을 포함합니다.  

```go
// 백엔드 기술 스택: Go 1.24.5 + Wails v2 (gopsutil, nvidia-smi 통합)
// 프론트엔드 기술 스택: React 18 + TypeScript + Zustand + react-grid-layout
```