---
Language: JavaScript
tags:
 - Reflect-Metadata
 - 데코레이터
 - 리플렉션
 - 메타데이터
 - TypeScript
aliases:
 - reflect-metadata
 - Reflect.Metadata
 - reflect-metadata-api
 - 메타데이터-리플렉션
url: https://github.com/rbuckton/reflect-metadata
---
이 프로젝트는 JavaScript/TypeScript에서 클래스 및 멤버에 메타데이터를 추가하고 조회할 수 있는 `Reflect-Metadata` API를 제공합니다. TypeScript의 실험적 데코레이터와 호환되며, 레거시 `--experimentalDecorators` 옵션을 사용하는 프로젝트를 지원합니다. 표준 데코레이터가 도입되면서 표준화 제안은 중단되었지만, 기존 프로젝트와의 호환성을 위해 계속 유지보수되고 있습니다.

메타데이터를 선언적/명령형으로 정의 및 조회할 수 있으며, Composition, Dependency Injection, 런타임 타입 검증 등 다양한 사용 사례를 지원합니다. `Reflect` 객체를 확장하여 메타데이터 관리 기능을 제공하며, ES 모듈, CommonJS, 브라우저 환경 등 다양한 설정에서 사용할 수 있습니다.