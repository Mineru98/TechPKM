---
Language: Go
tags:
 - BaaS
 - REST API
 - 인증 시스템
 - 실시간 업데이트
 - 파일 기반 저장소
aliases:
 - Pennybase
 - 파이어베이스 대체
 - 간단한 BaaS
 - CSV 기반 데이터베이스
url: https://github.com/zserge/pennybase
---
Pennybase는 Go 언어로 구현된 가벼운 백엔드 서비스(BaaS)로, Firebase/Supabase와 유사한 핵심 기능을 제공합니다. CSV 파일 기반 저장소, REST API, RBAC 권한 시스템, 실시간 업데이트(SSE), 스키마 검증 등을 표준 라이브러리만으로 구현했습니다. 정적 자산 서빙과 템플릿 렌더링 기능을 지원하며, 훅 시스템을 통해 확장성이 가능합니다.  

주요 특징으로는:  
1. 버전 관리가 되는 CSV 파일 저장소  
2. 세션 쿠키와 Basic Auth 기반 인증  
3. 역할 기반 접근 제어(RBAC) 및 리소스 소유권 관리  
4. Go 템플릿을 이용한 HTML 렌더링  
5. 리소스 생성/수정/삭제 시 트리거되는 훅 시스템  

MIT 라이선스로 배포되며, 코드는 1000줄 미만으로 간결하게 유지되었습니다.