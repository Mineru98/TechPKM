---
Language: TypeScript
tags:
 - dependency-injection
 - typescript
 - javascript
 - inversion-of-control
 - container
aliases:
 - TypeDI
 - 타입디아이
 - 타입의존성주입
 - DI 컨테이너
url: https://github.com/typestack/typedi
---
TypeDI는 TypeScript와 JavaScript를 위한 의존성 주입 도구로, Node.js 또는 브라우저 환경에서 구조화되고 테스트 가능한 애플리케이션 개발을 지원합니다. 주요 기능으로는 프로퍼티 기반/생성자 기반 주입, 싱글톤/트랜지언트 서비스, 여러 DI 컨테이너 지원 등이 있습니다. Reflect-Metadata 라이브러리와 함께 사용하여 타입 정보를 기반으로 자동 의존성을 해결하며, 데코레이터 메타데이터 기반 구성 방식을 채택하고 있습니다.  

타입스크립트 프로젝트에서 사용할 경우 `reflect-metadata` 패키지와 데코레이터 옵션(`emitDecoratorMetadata`, `experimentalDecorators`)이 필수적으로 요구됩니다.