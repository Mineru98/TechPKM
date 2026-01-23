---
Language: Python  
tags:  
 - 1-bit Transformer  
 - 비트넷 구현  
 - 허깅페이스 트랜스포머  
 - 라마 아키텍처  
 - 양자화  
aliases:  
 - BitNet-Transformers  
 - 비트넷 트랜스포머  
 - 1비트 트랜스포머 구현  
 - BitLLAMA  
url: https://github.com/Beomi/BitNet-Transformers  
---
이 프로젝트는 "BitNet: Scaling 1-bit Transformers for Large Language Models" 논문의 파이션 구현체입니다. Huggingface Transformers 라이브러리에 Llama(2) 아키텍처를 기반으로 1비트 가중치를 활용하는 BitLinear 계층을 통합하여 GPU 메모리 사용량을 최적화한 모델입니다. 16비트 대비 200MB에서 100MB 수준의 메모리 효율성을 달성하면서 대규모 언어 모델 훈련 가능성을 탐구합니다. 주요 특징으로 양자화 기법, 비트넷 아키텍처, Wikitext-103 데이터셋 훈련 지원을 포함합니다.