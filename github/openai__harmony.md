---
Language: Python, Rust
tags:
 - OpenAI 모델 포맷
 - 채팅 인코딩/디코딩
 - 멀티채널 응답 처리
 - 함수 호출 지원
 - Rust-Python 바인딩
aliases:
 - harmony-openai
 - gpt-oss-포맷
 - openai-harmony
 - 채팅 형식 규격
url: https://github.com/openai/harmony
---
OpenAI Harmony는 gpt-oss 모델 시리즈에 사용되는 공식 응답 형식 사양 및 구현 라이브러리입니다. 이 프로젝트는 채팅 구조 정의, 추론 출력 생성, 다중 채널 응답 처리를 위한 표준화된 포맷을 제공하며, 특히 Python과 Rust로 구현된 고성능 인코딩/디코딩 솔루션을 포함합니다. Rust로 작성된 핵심 로직에 Python 바인딩을 제공해 개발자 친화적인 API를 지원하며, 함수 호출 및 도구 사용 시나리오에 최적화된 구조를 갖추고 있습니다.  

> 📌 **핵심 특징**:  
> - OpenAI 응답 API와 호환되는 포맷  
> - Rust 기반 고속 처리 + Python 편의성  
> - 멀티채널(분석/논평/최종응답) 및 함수 호출 지원  
> - 토큰 손실 없는 정확한 파싱 기능