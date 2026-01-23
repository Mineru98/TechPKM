---
Language: Python  
tags:  
 - 프롬프트 압축  
 - 대규모 언어 모델  
 - LLM 최적화  
aliases:  
 - LLMLingua 시리즈  
 - 프롬프트 압축 도구  
 - LLM 효율성 향상  
url: https://github.com/microsoft/LLMLingua  
---  
LLMLingua 시리즈는 대규모 언어 모델(LLM)의 프롬프트 효율성을 향상시키기 위한 도구입니다. GPT2-small 또는 LLaMA-7B와 같은 소형 모델을 활용해 프롬프트 내 불필요한 토큰을 제거함으로써, 최대 20배의 압축률을 달성하면서도 성능 손실을 최소화합니다. 이 시리즈는 LongLLMLingua(장문 처리 최적화), LLMLingua-2(작업-불문 압축), SecurityLingua(보안 강화) 등 다양한 변형을 포함하며, RAG, 온라인 회의, 코드 분석 등 실제 시나리오에서 LLM의 컨텍스트 지원, 비용 절감, 추론 속도 향상을 가능하게 합니다.  

LLMLingua-2는 GPT-4 기반 데이터 증류를 통해 훈련되어 3~6배 빠른 속도와 우수한 도메인 적응력을 제공하며, SecurityLingua는 프롬프트 압축을 통해 LLM의 탈옥 공격을 방어하는 효율적인 보안 메커니즘을 구현했습니다. 프로젝트는 pip 설치와 파이썬 API를 통해 쉽게 활용할 수 있으며, LangChain 및 LlamaIndex와의 통합을 지원합니다.