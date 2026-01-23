---
Language: Python
tags:
 - 토큰 분석
 - LLM 토크나이저
 - 한글 처리
 - 가중치 조정
aliases:
 - Llama4-Token-Editor
 - 한국어 토큰 조정 도구
url: https://github.com/sionic-ai/Llama4-Token-Editor
---
LLaMA Token Editor는 대형 언어 모델(LLM)의 토크나이저를 분석하고 특정 토큰 가중치를 조정하는 도구입니다. 주로 Llama 및 Qwen 계열 모델의 한글/영어 토큰을 분석하며, 완성도 높은 한글 표현과 가중치 조정을 지원합니다. UTF-8 인코딩과 BPE 알고리즘 역공학을 통해 한글 토큰을 식별하고, 토크나이저의 표현력을 개선하는 데 활용됩니다.  

| 분석 항목 | Llama-4-Scout-17B | Llama-3.3-70B-Instruct | Qwen2.5-32B |
|-----------|------------------|------------------------|-------------|
| 한글 가능성 토큰 수 | 64,992 | 25,738 | 53,204 |
| 완성형 한글 포함 토큰 수 | 5,490 | 2,281 | 3,498 |  

주요 기능으로는 토큰 카테고리 분석(순수 영문, 한글 가능성, 완성형 한글 등)과 가중치 조정(`categorized_token_ids.txt` 증가, `uncategorized_token_ids.txt` 감소)이 포함됩니다.  
지원 모델: Llama-4-Scout-17B, Llama-3.3-70B-Instruct, Qwen2.5-32B. MIT License 적용.