---
Language: Python  
tags:  
 - Mixture-of-Experts  
 - Continual Pre-training  
 - LLaMA  
 - MoE 모델  
 - 자연어 처리  
aliases:  
 - LLaMA-MoE  
 - LLaMA MoE  
 - LLaMA MoE 모델  
url: https://github.com/pjlab-sys4nlp/llama-moe  
---
LLaMA-MoE는 LLaMA와 SlimPajama 데이터셋을 기반으로 구축된 오픈소스 Mixture-of-Experts(MoE) 모델 시리즈입니다. 주요 특징은 경량화 설계(활성화 파라미터 3.0~3.5B), 다양한 전문가 구성 방법(클러스터링/그래디언트 기반), 효율적인 지속적 사전 학습(FlashAttention-v2 통합) 등입니다. HuggingFace에서 모델 가중치를 제공하며, 평가 결과 기존 모델 대비 우수한 성능을 보입니다.  

핵심 기술로는 Top-K 게이팅, 동적 가중치 샘플링, 전문가 균형 모니터링 도구를 포함하며, 연구 및 배포 친화적인 설계가 특징입니다. 논문, 기술 보고서, 코드 예제, 설치 가이드를 통해 모델 활용 방법을 상세히 설명합니다.