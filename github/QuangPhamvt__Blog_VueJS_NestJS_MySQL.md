---
Language: JavaScript
tags:
 - Vue 3
 - NestJS
 - MySQL
 - TypeORM
 - 인증 시스템
aliases:
 - 회사 인턴 프로젝트
 - 블로그 웹 앱
 - Vue-NestJS 통합 프로젝트
url: https://github.com/vfa-quangpm1/DEMO
---
이 프로젝트는 회사 인턴십을 위해 개발된 개인 기술 블로그 웹 애플리케이션입니다. Vue 3 기반 프론트엔드와 NestJS 기반 백엔드를 결합하여 사용자 인증(로그인/로그아웃/회원가입), 블로그 포스트 작성 및 카테고리 관리 기능을 제공합니다. 프론트엔드는 Vite와 Sass를 사용하며, 백엔드는 TypeORM과 MySQL을 통해 데이터를 관리합니다.

### 주요 특징
1. **프론트엔드**: Vue 3 + Vue Router + Pinia + Sass
2. **백엔드**: NestJS + Passport 인증 + JWT 토큰 관리
3. **데이터베이스**: MySQL + TypeORM
4. **기능**: 관리자 전용 포스트 작성, 마크다운 지원, 리프레시 토큰 기반 인증 시스템

### 기술 스택
- **프론트엔드**: Vue 3, Vite, Sass, Axios, Marked.js
- **백엔드**: NestJS, TypeORM, MySQL2, Bcrypt, Passport-JWT
- **기타**: JWT 인증, CORS 설정, Swagger API 문서화

### 핵심 기능
- 사용자 역할 기반 접근 제어(관리자/일반 사용자)
- 마크다운 지원 포스트 작성 및 렌더링
- 리프레시 토큰을 통한 세션 관리
- 카테고리 기반 포스트 관리 시스템