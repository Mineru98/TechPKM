---
Language: Go
tags:
 - Redis 클라이언트
 - 캐싱
 - 파이프라인 처리
 - 분산 시스템
 - Go 라이브러리
aliases:
 - valkey-go
 - 발레키 클라이언트
 - Go Redis 대안
 - 발레키 자동 파이프라이닝
url: https://github.com/valkey-io/valkey-go
---
valkey-go는 고성능 Redis(Valkey) 클라이언트 라이브러리로, 자동 파이프라이닝과 서버 지원 클라이언트 측 캐싱 기능을 제공합니다. Go 언어로 작성되었으며, 다양한 Redis 명령어에 대한 개발자 친화적인 빌더와 분산 잠금, 캐시 어사이드 패턴, OpenTelemetry 통합 등의 고급 기능을 지원합니다. Redis 클러스터, 센티넬, 다양한 Redis 모듈(검색, 스트림, 확률적 자료구조 등)과 호환되며, Google Cloud Memorystore와 같은 서비스에서도 사용 가능합니다.