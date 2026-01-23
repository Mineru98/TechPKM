---
Language: Python  
tags:  
 - 한국어-LLM  
 - 멀티태스크-지도학습  
 - 인스트럭션-튜닝  
 - 오픈소스-모델  
 - 한국어-NLP  
aliases:  
 - KO-MT-Instruction-Tuning  
 - Komt  
 - davidkim205-komt  
 - 한국어-멀티태스크-튜닝  
 - KO-LLM-튜닝  
url: https://github.com/davidkim205/komt  
---  
**Komt**는 한국어 성능 향상을 위해 다양한 작업의 감독 데이터셋을 활용한 멀티태스크 인스트럭션 튜닝 기법을 도입한 연구 프로젝트입니다. ChatGPT와 같은 대규모 언어 모델의 성공에도 불구하고 한국어 처리에서 발생하는 한계를 극복하기 위해 설계되었으며, Llama2 및 Mistral 기반 모델을 최적화해 공개했습니다. 7B~30B 파라미터 규모의 오픈소스 모델을 제공하며, DPO(Direct Preference Optimization)를 적용한 버전은 76.75%의 성능으로 GPT-3.5-turbo(79.45%)에 근접한 결과를 달성했습니다. 텍스트 생성, 파인튜닝, 다양한 추론 인터페이스(text-generation-webui, llama.cpp 등)를 지원합니다.