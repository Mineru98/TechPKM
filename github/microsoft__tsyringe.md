---
Language: TypeScript
tags:
 - 의존성 주입
 - DI 컨테이너
 - TypeScript
 - JavaScript
 - constructor injection
aliases:
 - TSyringe
 - tsyringe
 - typescript-dependency-injection
url: https://github.com/Microsoft/tsyringe
---
TSyringe는 TypeScript/JavaScript를 위한 경량 의존성 주입(DI) 컨테이너입니다. 생성자 주입(Constructor Injection)을 지원하며, 데코레이터와 컨테이너를 통해 의존성 관리를 간소화합니다. 싱글톤, 스코프드 등록, 변환기 주입, 원시 값 주입 등을 포함한 다양한 기능을 제공하며, 순환 의존성 문제 해결 및 비동기 처리도 지원합니다. Reflect API와 호환되도록 구성되어 있으며, Babel 환경에서도 사용할 수 있습니다.  

주요 기능: 데코레이터 기반 의존성 주입, 컨테이너 레지스트리, 인터셉션, 자식 컨테이너, 인스턴스 초기화/해제 기능 등.