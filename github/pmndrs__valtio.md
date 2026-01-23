---
Language: JavaScript
tags:
 - React 상태 관리
 - Proxy 기반
 - 경량 라이브러리
 - 실시간 상태 동기화
 - Vanilla JS 지원
aliases:
 - valtio 상태 관리
 - 프록시 기반 상태
 - React valtio
 - 경량 상태 관리
url: https://github.com/pmndrs/valtio/blob/main/README.md
---
Valtio는 JavaScript 객체를 프록시 기반 반응형 상태로 변환하는 경량 상태 관리 라이브러리입니다. React 환경에서 최적화된 렌더링과 실시간 상태 동기화를 제공하며, 일반 객체 조작 방식으로 상태를 변경할 수 있습니다. `useSnapshot` 훅을 통해 필요한 부분만 업데이트되며, React 19의 Suspense 및 Vanilla JS 환경에서도 사용 가능합니다. Redux DevTools와의 호환성을 통해 디버깅을 지원하며, Set/Map과 같은 복잡한 데이터 구조도 처리할 수 있습니다.