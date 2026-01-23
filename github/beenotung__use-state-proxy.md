---
Language: TypeScript
tags:
 - React 상태 관리
 - Proxy API
 - 상태 변경 감지
 - 커스텀 클래스 지원
 - 오픈소스 라이브러리
aliases:
 - use-state-proxy
 - 리액트 프록시 상태
 - 자동 리렌더링
url: https://github.com/yourusername/use-state-proxy
---
이 프로젝트는 React의 `useState()` 훅에 Proxy API를 적용하여 상태 변경을 자동으로 감지하고 리렌더링을 트리거하는 라이브러리입니다. 배열, Map, Set, Date, 객체 및 커스텀 클래스의 변형 메서드를 직접 호출해도 자동으로 상태 업데이트를 처리하며, 기존 `useState()` 대비 복잡한 데이터 타입 업데이트 시 발생하는 번거로움을 해소합니다. BSD-2-Clause 라이선스로 배포되는 오픈소스 라이브러리입니다.