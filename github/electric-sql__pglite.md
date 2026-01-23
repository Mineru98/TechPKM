---
Language: JavaScript/TypeScript
tags:
 - WebAssembly
 - Postgres
 - WASM
 - 데이터베이스
 - 로컬퍼스트앱
aliases:
 - PGlite
 - PostgresWASM
 - 전기SQL
url: https://github.com/electric-sql/pglite
---
PGlite는 WebAssembly(WASM)로 빌드된 Postgres 데이터베이스로, 브라우저, Node.js, Bun, Deno 환경에서 의존성 없이 사용할 수 있는 경량 솔루션입니다. 3MB(압축) 크기로 pgvector 확장 등을 지원하며, 인메모리 또는 파일 시스템/인덱시DB에 영구 저장 가능합니다. 로컬 퍼스트 앱 개발에 최적화되어 있으며, 기존 "브라우저 내 Postgres" 프로젝트와 달리 리눅스 가상 머신을 사용하지 않습니다.  

주요 기능은 단일 사용자/연결 제한, TypeScript 클라이언트 라이브러리 제공, 다양한 플랫폼(CDN, NPM, Bun/Deno 지원)입니다. Apache 2.0 또는 PostgreSQL 라이선스 중 선택 적용 가능합니다.