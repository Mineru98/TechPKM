---
Language: TypeScript
tags:
 - Postgres
 - WASM
 - WebAssembly
 - Local-first
 - Realtime
aliases:
 - PGlite
 - pgLite
 - PostgresWASM
 - WASMPostgres
 - 로컬퍼스트DB
url: https://github.com/electric-sql/pglite
---
PGlite는 웹 브라우저, Node.js, Bun, Deno 환경에서 Postgres를 WASM(WebAssembly)으로 실행할 수 있게 하는 TypeScript 라이브러리입니다. PostgreSQL의 단일 사용자 모드를 기반으로 하여 3MB(압축 크기)로 경량화되었으며, pgvector 같은 확장 기능을 지원합니다. 인메모리 데이터베이스 또는 파일 시스템/IndexedDB를 통한 지속성이 가능합니다.

PGlite는 리눅스 가상 머신 없이 순수 WASM으로 PostgreSQL을 구동하며, 실시간 로컬퍼스트 애플리케이션 개발에 최적화되었습니다. Apache 2.0 또는 PostgreSQL 라이선스 중 선택적으로 적용 가능합니다.