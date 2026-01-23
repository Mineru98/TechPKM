---
Language: Python  
tags:  
 - NumPy  
 - LLM 구현  
 - 자연어 처리  
aliases:  
 - llama3.np  
 - 라마3 넘파이 구현  
 - 순수 넘파이 LLM  
url: https://github.com/likejazz/llama3.np  
---  
`llama3.np`는 Llama 3 모델을 순수 NumPy로 구현한 프로젝트입니다. Andrej Karpathy의 stories15M 모델을 기반으로 정확한 구현을 목표로 하며, 학술 연구나 교육용 LLM 구현 분석에 적합합니다. NumPy만으로 트랜스포머 아키텍처를 재현하여 하드웨어 제약 없는 실험을 가능하게 합니다.  

이 프로젝트는 CUDA 기반 구현체와 달리 CPU 환경에서도 LLM의 내부 작동 원리를 탐구하기 위한 참고 자료로 활용됩니다. 주요 기능으로는 텍스트 생성, 토크나이징, 로터리 임베딩 처리 등이 포함됩니다.