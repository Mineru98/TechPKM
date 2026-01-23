---
Language: Go
tags:
 - ARM64 컴파일러
 - 고성능 컴퓨팅
 - Go 최적화
 - 하드웨어 튜닝
 - 임베드 시스템
aliases:
 - gARM
 - ARM64 Go 컴파일러
 - 고퍼 컴파일러
url: https://github.com/bornmay/gARM
---
`gARM彡`는 Go의 간결성과 ARM64 아키텍처의 저수준 제어를 결합한 고성능 컴파일러입니다. ARMv8 명령어 세트(예: 조건부 실행, NEON SIMD, 하드웨어 연산)의 특성을 최적화하여 ARM 기반 서버/임베드 시스템에서 5배 이상의 성능 향상을 목표로 합니다. 다양한 GC 알고리즘 선택과 하드웨어 튜닝 기능을 제공하며, Apple M-Series, AWS Graviton 등 ARM64 생태계 전반에 적용 가능합니다. AST-SSA-IR 파이프라인 기반 최적화 기술을 핵심으로 합니다.