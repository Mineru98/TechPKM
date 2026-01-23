---
Language: Rust  
tags:  
 - LLM 추론 엔진  
 - 멀티모달  
 - 고속 인퍼런스  
aliases:  
 - mistral.rs  
 - 고속 LLM 추론  
 - 멀티모달 AI 엔진  
url: https://github.com/EricLBuehler/mistral.rs  
---  
**mistral.rs**는 텍스트, 비전, 이미지 생성, 음성 모델을 지원하는 초고속 크로스플랫폼 LLM 추론 엔진입니다. OpenAI 호환 HTTP 서버, Rust/Python API, MCP(Multimodal Context Protocol) 서버 기능을 제공하며, ISQ, PagedAttention, FlashAttention 등 최적화 기술로 성능을 극대화합니다. Qwen 3, Llama 3, Gemma 3 등 다양한 최신 모델 지원 및 레이어 별 토폴로지 최적화, 외부 도구 자동 연동(MCP 클라이언트) 기능을 갖추고 있습니다.  

핵심 기능:  
1. 텍스트↔텍스트, 멀티모달(텍스트+비전+오디오)↔텍스트, 음성/이미지 생성  
2. CPU/GPU 가속 및 자동 분산 처리  
3. 레이어 별 양자화 및 장치 배치 최적화  
4. 웹 검색 통합, 실시간 도구 호출 지원  
5. OpenAI 호환 API 및 MCP 프로토콜 지원  

주요 지원 모델: Qwen 3, Llama 3, Gemma 3, Mistral, FLUX(이미지 생성), Dia(음성 생성) 등.