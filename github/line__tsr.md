---
Language: TypeScript
tags:
 - TypeScript
 - 코드 정리
 - 정적 분석
 - 미사용 코드 제거
 - 트리 쉐이킹
aliases:
 - tsr
 - TypeScript Remove
 - 미사용 코드 검출
 - 코드 정리 도구
url: https://github.com/tsrorg/tsr
---
이 프로젝트는 TypeScript 프로젝트에서 사용되지 않는 코드를 제거하는 도구입니다. 번들러의 트리 쉐이킹과 유사하게 정적 분석을 통해 사용되지 않는 내보내기 및 파일을 식별하며, CI 파이프라인에서 미사용 코드를 감지할 수 있습니다. 현재는 프로젝트가 종료되었으며, 유사한 기능을 위해 Knip 같은 도구를 권장합니다. TypeScript 컴파일러와 `tsconfig.json` 설정을 기반으로 동작하며, 최소한의 설정으로 빠르게 사용할 수 있습니다. CLI 또는 JavaScript API를 통해 미사용 코드를 검출하거나 자동으로 제거할 수 있습니다.