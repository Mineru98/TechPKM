---
Language: Python
tags:
 - 구조화된 출력
 - LLM
 - Python 라이브러리
 - 스키마 기반 생성
 - 구조화된 생성
aliases:
 - outlines 라이브러리
 - .txt AI
 - 구조화된 LLM 출력
 - 파이썬 타입 시스템
 - Pydantic 모델
url: https://github.com/dottxt-ai/outlines/blob/main/README.md
---
Outlines는 LLM의 출력을 구조화된 형식으로 보장하기 위한 Python 라이브러리입니다. "XML, FHIR, 사용자 정의 스키마 등 구조화된 출력이 필요한 경우" 다양한 모델(OpenAI, Ollama, vLLM 등)과 호환되며, 파이썬 타입 시스템 또는 Pydantic 모델을 통해 출력 구조를 정의합니다. 간단한 통합(예: `model(prompt, output_type)`)으로 유효성이 검증된 구조를 제공하며, 코드 변경 없이 모델을 전환할 수 있는 유연성을 갖추었습니다. NVIDIA, Cohere 등 주요 기업에서 신뢰하는 솔루션으로, 고객 지원 트리아지, 전자상거래 제품 분류 등 실제 사례에 적용 가능합니다.