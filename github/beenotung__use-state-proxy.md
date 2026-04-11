---
Language: TypeScript
tags:
 - React
 - StateManagement
 - Proxy
 - Hooks
 - JavaScript
aliases:
 - useStateProxy
 - use-state-proxy
url: https://github.com/beenotung/use-state-proxy/blob/master/README.md
---
React의 Proxy API를 활용하여 상태 업데이트 시 별도의 setState 호출 없이도 자동으로 재렌더링을 트리거하는 상태 관리 라이브러리입니다. 배열, Map, Set 등 복합 데이터 타입의 변경 메서드를 직접 호출할 수 있어 기존 useState의 불변성 유지로 인한 보일러플레이트 코드를 크게 줄여줍니다. 사용자 정의 클래스의 변이 메서드도 등록하여 사용할 수 있도록 확장성을 제공합니다.