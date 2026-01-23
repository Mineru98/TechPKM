---
Language: Python
tags:
 - 양자화
 - LLaMA
 - GPTQ
 - 언어모델
 - CUDA
aliases:
 - GPTQ-LLaMA
 - LLaMA-양자화
 - 4비트-양자화
url: https://github.com/camenduru/GPTQ-for-LLaMa/blob/cuda/README.md
---
이 프로젝트는 LLaMA 언어 모델을 4비트 양자화하는 GPTQ 기술을 구현한 리포지토리입니다. GPTQ는 단일 패스 가중치 양자화 방법으로, 대규모 모델의 메모리 사용량을 크게 줄이면서도 성능 저하를 최소화합니다. CUDA 기반 커널 최적화로 생성 속도를 향상시켰으며, LLaMA-7B부터 65B까지의 다양한 모델 크기에 대한 양자화 결과를 제공합니다. 주요 특징으로는 활성화 순서 기반 양자화(--act-order), 순차적 양자화(--true-sequential) 등이 포함됩니다.  

**요약**:  
LLaMA 모델을 4/3비트 양자화하는 GPTQ 기술 구현체. CUDA 가속 및 메모리 최적화 기능을 통해 대형 언어 모델의 효율적인 배포를 지원합니다. 다양한 모델 크기와 양자화 설정에 대한 성능 비교 데이터를 포함합니다.