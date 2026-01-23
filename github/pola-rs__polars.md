---
Language: Rust
tags:
 - DataFrame
 - Query Engine
 - Rust
 - Python
 - High Performance
aliases:
 - Polars
 - Rust DataFrame
 - 고속 데이터 처리
url: https://github.com/pola-rs/polars
---
Polars는 Rust로 작성된 초고속 DataFrame 쿼리 엔진으로, Lazy/Eager 실행, 스트리밍 처리, 멀티스레딩, SIMD 최적화 등의 기능을 제공합니다. Python/Rust/Node.js/R/SQL 프론트엔드를 지원하며, 대용량 데이터 처리에 최적화되어 있습니다. Apache Arrow 형식과 호환되며, 메모리 효율성과 확장성을 강점으로 합니다.  

### 주요 특징:
- **초고속 성능**: PDS-H 벤치마크에서 우수한 성능 입증
- **경량성**: NumPy/Pandas 대비 빠른 로딩 속도
- **대용량 데이터 지원**: RAM을 초과하는 데이터 처리 가능(collect(engine='streaming') 활용)
- **다양한 언어 지원**: Python/Rust/Node.js/R/SQL 바인딩 제공

> 주요 사용 사례: 데이터 분석, ETL 파이프라인, 대용량 데이터 처리 시스템