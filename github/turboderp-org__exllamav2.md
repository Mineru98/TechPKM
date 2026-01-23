---
Language: Python  
tags:  
 - 로컬 LLM 추론  
 - GPU 최적화  
 - 4비트 양자화  
 - Flash Attention  
 - 오픈소스 라이브러리  
aliases:  
 - ExLlamaV2  
 - 로컬 LLM 실행  
 - GPU 기반 LLM  
 - EXL2 양자화  
url: https://github.com/turboderp-org/exllamav2  
---
ExLlamaV2는 소비자 GPU에서 로컬 LLM 추론을 가능하게 하는 고성능 파이썬 라이브러리입니다. Paged Attention과 Flash Attention 2.5.7+를 지원하며, 동적 배치 처리, 프롬프트 캐싱, K/V 캐시 중복 제거 등의 기능을 포함한 새로운 생성기를 제공합니다. GPTQ 및 자체 개발한 EXL2 양자화 형식(2~8비트)을 지원하여 메모리 효율성과 성능을 균형 있게 구현합니다. TabbyAPI, text-generation-webui 등 다양한 프론트엔드와 통합될 수 있으며, Llama, CodeLlama, OpenLlama 등 주요 LLM 아키텍처를 포괄적으로 지원합니다.