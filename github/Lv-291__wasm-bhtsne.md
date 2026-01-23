---
Language: Rust/Wasm
tags:
 - t-SNE
 - 웹최적화
 - 멀티스레딩
 - 데이터시각화
 - WASM
aliases:
 - wasm-bhtsne
 - web-tsne
 - tsne-wasm
url: https://github.com/Lv-291/wasm-bhtsne
---
이 프로젝트는 브라우저에서 고성능 t-SNE 알고리즘을 실행할 수 있도록 WASM(WebAssembly)으로 구현된 라이브러리입니다. Rust 기반의 bhtsne를 WASM으로 변환하여 멀티스레딩 지원과 유동적인 하이퍼파라미터 조정이 가능하며, 대용량 데이터의 시각화 및 점진적 임베딩 최적화에 특화된 솔루션입니다. JavaScript API를 통해 Float32/Float64 데이터 입력과 반복 기반 알고리즘 실행이 가능합니다.  

```markdown
### 핵심 기능
- `wasm-bindgen-rayon`을 활용한 웹 멀티스레딩 지원
- 기본값 대체 가능한 유연한 하이퍼파라미터 구성
- `SharedArrayBuffer` 기반 병렬 처리 (COOP/COEP 정책 필요)
- 점진적 임베딩 개선(iterative refinement) 기능
```