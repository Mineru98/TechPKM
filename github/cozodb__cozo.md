---
Language: Rust  
tags:  
 - 그래프 데이터베이스  
 - Datalog  
 - 임베디드 데이터베이스  
 - 벡터 검색  
 - 시계열 데이터  
aliases:  
 - CozoDB  
 - 코조DB  
 - Datalog 그래프 데이터베이스  
url: https://github.com/cozodb/cozo  
---  
CozoDB는 **Datalog** 기반의 범용 트랜잭션 관계형 데이터베이스로, 그래프 데이터 처리와 알고리즘에 특화된 임베디드 솔루션입니다. SQLite처럼 동일 프로세스에서 실행되며, HNSW 기반 벡터 검색, MinHash-LSH, 풀텍스트 검색 등을 지원합니다. 시간 여행 기능으로 데이터 변경 이력 추적이 가능하며 RocksDB, SQLite 등 다양한 스토리지 엔진과 호환됩니다. Rust로 구현되어 높은 성능을 제공하며, 웹 어셈블리(WASM)를 통해 브라우저에서도 사용 가능합니다.