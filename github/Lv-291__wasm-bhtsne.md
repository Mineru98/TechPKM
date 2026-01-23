---
Language: Rust
tags:
 - t-SNE
 - WebAssembly
 - 멀티스레딩
 - JavaScript 바인딩
 - 시각화 데이터 처리
aliases:
 - wasm-bhtsne
 - t-SNE WebAssembly
 - WebAssembly t-SNE
url: https://github.com/frjnn/bhtsne
---
이 프로젝트는 Rust로 구현된 `bhtsne` 라이브러리를 WebAssembly로 변환하여 웹 환경에서 고성능 t-SNE 알고리즘을 실행할 수 있게 합니다. 멀티스레딩을 지원하여 대규모 데이터셋의 시각화를 가속화하며, JavaScript 객체를 통해 하이퍼파라미터를 유연하게 조정할 수 있습니다. `Float32Array` 및 `Float64Array` 입력을 지원하며, 점진적 임베딩 개선을 위한 반복 실행 기능을 제공합니다.  

MIT 라이선스로 배포되며, 웹에서 멀티스레딩 기능을 사용하려면 `SharedArrayBuffer`와 cross-origin 격리 정책을 활성화해야 합니다. `wasm-feature-detect` 라이브러리와 함께 사용하여 브라우저 호환성을 확인할 수 있습니다.