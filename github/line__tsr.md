---
Language: TypeScript
tags:
 - TypeScript
 - 코드 정리
 - 미사용 코드 제거
 - 트리 쉐이킹
 - 정적 분석
aliases:
 - tsr
 - typescript-remove-unused
 - 타입스크립트 미사용 코드 제거
url: https://github.com/line/tsr
---
TypeScript Remove(tsr)는 TypeScript 프로젝트에서 미사용 코드를 제거하는 유틸리티입니다. 번들러에서의 트리 쉐이킹과 유사하게 정적 분석을 통해 프로젝트에서 사용되지 않는 내보내기(exports)와 파일(모듈)을 식별하고, CI 파이프라인에서 미사용 코드 추가를 감지하는 데 사용됩니다. 간단한 `tsconfig.json` 설정으로 자동 코드 제거가 가능하며, 재귀적 편집과 테스트 파일 보호 기능을 지원합니다. 프로젝트 중단 상태이며 유사 툴인 Knip 사용을 권장합니다.