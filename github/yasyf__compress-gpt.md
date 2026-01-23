---
Language: Python
tags:
 - 토큰 최적화
 - 프롬프트 압축
 - LLM 효율화
 - langchain 통합
 - AI 비용 절감
aliases:
 - CompressGPT
 - GPT 프롬프트 압축
 - 토큰 절약 도구
 - CompressTemplate
url: https://github.com/yathian/compress-gpt
---
CompressGPT는 프롬프트 토큰 사용량을 최대 70%까지 줄이기 위한 자체 압축 기술을 제공하는 Python 라이브러리입니다. LangChain의 `PromptTemplate`을 대체하여 변수 삽입 전후로 프롬프트를 압축할 수 있으며, 압축 실패 시 원본 프롬프트를 그대로 사용합니다. 캐싱 메커니즘으로 반복적인 압축 연산을 최적화하여 LLM 기반 애플리케이션의 운영 비용을 대폭 절감합니다. 

주요 기능: 
1. `CompressTemplate`(변수 삽입 전 압축) 및 `CompressPrompt`(변수 삽입 후 압축) 지원
2. 간단한 프롬프트용 `CompressSimplePrompt` 제공
3. 실패 시 자동 폴백(fallback) 및 캐시 관리 기능 내장