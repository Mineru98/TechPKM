---
Language: Python  
tags:  
 - 모델 병합  
 - 언어 모델  
 - 오픈소스 도구  
 - 머신러닝  
 - LLM 최적화  
aliases:  
 - mergekit  
 - 모델 병합 도구  
 - LLM 병합  
 - 언어 모델 통합  
url: https://github.com/arcee-ai/mergekit/blob/main/README.md  
---
`mergekit`는 사전 훈련된 언어 모델을 병합하기 위한 도구 모음입니다. CPU 또는 소량의 VRAM(8GB 이상)으로도 고급 병합 작업을 수행할 수 있는 **아웃오브코어 접근법**을 사용하며, 다양한 병합 알고리즘을 지원합니다. 모델은 Llama, Mistral, GPT-NeoX 등 다양한 아키텍처를 지원하며, **CPU/GPU 환경**에서 메모리 효율적인 병합이 가능합니다. 주요 기능으로는 레이어 조각 병합, LoRA 추출, Mixture of Experts(MoE) 병합, 다단계 병합 워크플로우 등이 포함됩니다.  

이 도구는 가중치 공간에서 직접 연산을 수행하여, 여러 모델의 강점을 결합하거나 새로운 기능을 생성하는 등 **추론 비용을 유지하면서 성능 향상**을 목표로 합니다. Hugging Face와 호환되는 모델 카드 생성, 커스텀 토크나이저 매핑, 병합 파라미터 조건부 지정 등 고급 기능을 제공합니다.