---
Language: Rust
tags:
 - semantic_caching
 - Redis_8
 - LLM_optimization
 - vector_search
 - HTMX_dashboard
aliases:
 - Latency_Slayer
 - 시맨틱_캐시
 - LLM_latency_reduction
 - Redis_HNSW
url: https://github.com/yourusername/latency-slayer
---
Latency Slayer는 Redis 8의 벡터 검색(HNSW + 코사인 유사도)을 활용해 LLM 답변을 시맨틱하게 캐싱하는 Rust 기반 웹 서비스입니다. OpenAI 임베딩과 연동해 유사 질문 탐지 시 캐시된 답변을 반환하며, 필드 수준 TTL과 실시간 메트릭스 대시보드를 지원합니다. 캐시 히트율, 응답 지연 시간(p50/p95) 모니터링을 통해 효율적인 LLM 운영이 가능합니다.  

*참고: 실제 GitHub URL은 사용자가 제공한 README에 명시되지 않아 플레이스홀더가 사용되었습니다.*