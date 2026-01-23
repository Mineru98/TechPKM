---
Language: Go
tags:
 - BaaS
 - Firebase 대안
 - 파일 기반 저장소
 - REST API
 - 실시간 업데이트
aliases:
 - Pennybase
 - 가난한 사람을 위한 BaaS
 - CSV 기반 백엔드
url: https://github.com/yourusername/pennybase
---
Pennybase는 CSV 파일 기반의 경량 백엔드 서비스(BaaS) 구현체입니다. Firebase/Supabase와 유사한 핵심 기능(REST API, 인증, RBAC, 실시간 업데이트)을 1000줄 미만의 Go 코드로 구현했으며, 외부 의존성 없이 표준 라이브러리만 사용합니다. 데이터 저장소는 인간 친화적인 CSV 형식으로 관리되며, 스키마 검증 및 템플릿 렌더링 기능을 지원합니다. 정적 자산 호스팅과 확장 가능한 훅 시스템을 통해 기능 확장이 가능합니다.