---
Language: Python  
tags:  
 - DuckDB  
 - 분산처리  
 - 대용량데이터  
 - 데이터프레임  
 - MIT라이선스  
aliases:  
 - smallpond  
 - 딥시크AI-smallpond  
 - DuckDB프레임워크  
 - 분산데이터처리  
url: https://github.com/deepseek-ai/smallpond  
---
smallpond는 DuckDB와 3FS를 기반으로 구축된 경량 데이터 처리 프레임워크입니다. PB 규모의 데이터셋까지 확장 가능한 고성능 처리와 별도의 서비스 없이 간편하게 운영할 수 있는 것이 특징입니다. 파이썬 3.8~3.12 버전을 지원하며, 분산 환경에서의 데이터 처리 및 분석 작업에 최적화되어 있습니다.  

### 핵심 기능  
- DuckDB 기반의 고속 데이터 처리  
- 50개 컴퓨팅 노드 + 25개 스토리지 노드 환경에서 110.5TiB 데이터 30분 내 정렬  
- 파티셔닝, SQL 적용, Parquet 형식 입출력 등 직관적 데이터 조작  

### 사용 사례  
```python  
df = sp.partial_sql("SELECT ticker, min(price), max(price) FROM {0} GROUP BY ticker", df)  
```  
문서 및 성능 벤치마크는 공식 GitHub 저장소에서 확인 가능합니다.