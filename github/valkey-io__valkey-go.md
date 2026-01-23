---
Language: Go
tags:
 - Valkey 클라이언트
 - 캐싱
 - 분산 시스템
 - Go 라이브러리
 - Redis 호환
aliases:
 - valkey-go
 - Valkey Go 클라이언트
 - Go 캐싱 라이브러리
url: https://github.com/valkey-io/valkey-go
---
valkey-go는 Valkey(Valkey 호환 Redis)와 연동하기 위한 고성능 Go 클라이언트 라이브러리입니다. 자동 파이프라인을 지원하며, 서버 지원 클라이언트 측 캐싱, 분산 락, OpenTelemetry 통합 등의 기능을 제공합니다. RedisJSON, RedisBloom, RediSearch 등 다양한 Redis 모듈과 호환되며, 직관적인 명령어 빌더와 다양한 패턴(캐시-어사이드, 캐시-비활성화 등)을 지원합니다. Go-redis 대비 높은 처리량과 낮은 지연 시간을 특징으로 하며, 클러스터, 센티넬, 유니온 소켓 연결 등 다양한 배포 환경을 지원합니다.