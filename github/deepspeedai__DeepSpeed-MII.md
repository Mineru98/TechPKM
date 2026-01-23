---
Language: Python  
tags:  
 - 인퍼런스 최적화  
 - 대규모 언어 모델  
 - GPU 병렬 처리  
aliases:  
 - DeepSpeed-MII  
 - MII  
 - 고속 텍스트 생성  
 - 분산 인퍼런스  
url: https://github.com/deepspeedai/DeepSpeed-MII  
---
DeepSpeed-MII는 고성능 대규모 언어 모델 추론을 위한 오픈소스 Python 라이브러리입니다. 고속 처리, 저지연, 비용 효율성을 중점으로 설계되었으며, 블록된 KV 캐싱, 연속 배치 처리, 동적 SplitFuse, 고성능 CUDA 커널 등의 기술을 활용해 Llama-2-70B, Mixtral 8x7B 등의 모델에 대해 최대 2.5배 높은 처리량을 제공합니다. 3만7천 개 이상의 모델을 지원하며, Hugging Face와의 통합을 통해 모델 가중치와 토크나이저를 제공합니다. Python 휠 패키지로 쉽게 설치할 수 있으며, 비지속적/지속적 배포 옵션과 RESTful API를 통한 접근 기능을 포함합니다.