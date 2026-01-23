---
Language: Python  
tags:  
 - LLM 최적화  
 - 프롬프트 압축  
 - 자연어 처리  
aliases:  
 - LLMLingua 시리즈  
 - 프롬프트 압축 도구  
 - Microsoft LLMLingua  
url: https://github.com/microsoft/LLMLingua  
---  
LLMLingua 시리즈는 대규모 언어 모델(LLM)의 프롬프트 길이를 최대 20배까지 압축하는 도구입니다. GPT2-small이나 LLaMA-7B와 같은 소형 모델을 활용해 불필요한 토큰을 제거하며, 비용 절감과 긴 문맥 처리 성능 향상(예: "중간 손실" 문제 완화)을 목표로 합니다. LLMLingua, LongLLMLingua, LLMLingua-2, SecurityLingua 등 다양한 변형 모델이 제공되며, RAG, 온라인 회의, 코드 분석 등 실제 시나리오에서 활용 가능합니다. Hugging Face 데모와 LangChain/LlamaIndex 통합을 지원합니다.