---
Language: TypeScript
tags:
 - AI 백엔드 생성기
 - LLM 통합
 - Prisma ORM
 - NestJS
 - 자동화 개발
aliases:
 - AutoBE
 - AI 백엔드 빌더
 - 자동 백엔드 생성
url: https://github.com/wrtnlabs/autobe
---
AutoBE는 자연어 요구사항 분석을 통해 프로토타입부터 프로덕션까지 백엔드 애플리케이션을 자동으로 생성하는 AI 도구입니다. 요구사항 분석, 데이터베이스 설계, API 문서화, 테스트 커버리지, 타입 안전한 구현 로직을 제공하며, GPT-4.1 등 다양한 LLM 모델과 연동 가능합니다. 생성된 코드는 100% 빌드 가능하며, TypeScript/Prisma/NestJS 스택 기반으로 주니어 개발자 교육과 시니어 개발자 생산성 향상을 동시에 지원합니다.  

[기능 특징]  
- 챗봇 인터페이스로 요구사항 입력 → 백엔드 자동 생성  
- 요구사항 분석 보고서, ERD, Prisma 스키마, API 명세, E2E 테스트 포함  
- 타입 안전한 클라이언트 SDK 자동 생성 (프론트엔드 통합 용이)  
- 로컬 LLM 모델(qwen3 등) 지원 및 다중 LLM 공급자 호환  
- 생성된 코드는 MIT 라이선스 등 자유롭게 재배포 가능  

[현재 한계]  
- 런타임 동작은 테스트 필요(연동 문제, 예외 처리 등)  
- 복잡한 프로젝트는 250M+ 토큰 소모 가능(RAG 최적화 진행 중)  
- 유지보수 기능은 별도 개발 필요(Claude Code 등 AI 코파일럿과 연동 권장)  

[공식 문서]  
- 가이드: https://autobe.dev/docs/  
- 로드맵: https://autobe.dev/docs/roadmap/delta  
- 데모: http://localhost:5713/replay/index.html (로컬 실행 시)