---
Language: Python  
tags:  
 - 수학 추론 모델  
 - QLoRA 파인튜닝  
 - LLM 최적화  
 - Mathematical Reasoning  
 - Mistral-7B  
aliases:  
 - Arithmo2-Mistral-7B  
 - 수학 문제 해결 모델  
 - PoT(프로그램 출력 추론)  
 - CoT(연쇄적 추론)  
url: https://github.com/akjindal53244/Arithmo  
---  
Arithmo2-Mistral-7B는 수학 문제 해결 및 Python 프로그램 생성을 위한 경량화된 추론 모델입니다. Mistral-7B 기반에 4비트 QLoRA로 단일 GPU에서 파인튜닝되었으며, GSM8K(76.4%) 및 MATH(27.2%) 벤치마크에서 SOTA 성능을 달성했습니다. CoT(추론 단계 생성)와 PoT(프로그램 출력 기반 정답 검증) 방식을 지원하며, 데이터 중복 제거 및 NEFTune 적용으로 효율성을 개선했습니다. Apache-2.0 라이선스로 공개됩니다.