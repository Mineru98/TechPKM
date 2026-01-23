---
Language: Rust  
tags:  
 - full-stack-framework  
 - reactive-programming  
 - web-framework  
 - server-rendering  
 - isomorphic  
aliases:  
 - Leptos  
 - 렙토스  
 - Rust 웹 프레임워크  
 - Rust UI 프레임워크  
url: https://github.com/leptos-rs/leptos  
---
Leptos는 Rust로 작성된 풀스택 웹 프레임워크로, 세밀한 반응성과 선언적 UI 구축을 지원합니다. 클라이언트/서버 렌더링, 하이드레이션, 서버 함수 호출 등 다양한 웹 개발 시나리오를 단일 프레임워크에서 구현할 수 있습니다. Web 표준 기반 라우팅과 가상 DOM 없이 실제 DOM을 직접 조작하는 고성능 반응 시스템을 특징으로 합니다.  

### 핵심 기능  
- **풀스택 지원**: SSR(서버 사이드 렌더링), CSR(클라이언트 사이드 렌더링), 하이드레이션, HTML 스트리밍  
- **동형 프로그래밍**: 클라이언트와 서버에서 동일한 형태의 서버 함수 호출 가능  
- **세밀한 반응성**: 신호 변경 시 필요한 부분만 업데이트되는 최적화 시스템  
- **선언적 UI**: JSX 스타일 `view!` 매크로 또는 빌더 패턴 지원  

### 활용 분야  
- 웹 애플리케이션 개발  
- 서버 통합 UI 로직  
- 실시간 반응성 요구사항 구현  

### 생태계  
- `cargo-leptos` 빌드 도구 제공  
- Actix/Axum 기반 프로젝트 템플릿 지원  
- `awesome-leptos`를 통한 라이브러리/예제 공유