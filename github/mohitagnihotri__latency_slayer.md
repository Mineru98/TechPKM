---
Language: Rust  
tags:  
 - Semantic Caching  
 - Redis  
 - LLM  
 - Vector Search  
 - Real-time Metrics  
aliases:  
 - LatencySlayer  
 - SemanticCache  
 - LLM캐시  
 - Redis8벡터  
url: https://github.com/mohitagnihotri/latency_slayer  
---
Latency Slayer는 Redis 8의 벡터 검색 기능과 HNSW 알고리즘을 활용해 LLM(Large Language Model) 응답을 의미론적으로 캐싱하는 Rust 기반 웹 서비스입니다. 중복 유사 프롬프트에 대해 캐시된 답변을 반환하여 지연 시간을 줄이고, 필드 수준 TTL과 실시간 메트릭 대시보드를 지원합니다. OpenAI 임베딩과 연동되며, 캐시 히트율, p50/p95 지연 시간 등을 모니터링할 수 있습니다.  

주요 기능:  
- Redis 8 벡터 검색(HNSW + 코사인 유사도) 기반 의미론적 캐싱  
- 답변 필드에만 적용되는 TTL(TTL 시 벡터 데이터 유지)  
- 모델/경로별 필터링 및 실시간 메트릭 스트리밍  
- HTMX 기반 대시보드로 2초 간격 자동 갱신되는 히트율/지연 시간 시각화  

핵심 기술 스택: Rust, Redis 8, OpenAI API, HTMX.