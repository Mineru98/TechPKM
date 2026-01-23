---
Language: Python  
tags:  
 - RLHF  
 - 분산 컴퓨팅  
 - 딥러닝 교육  
 - Triton 커널  
 - 오픈소스 LLM  
aliases:  
 - 나노RLHF  
 - nanoRLHF  
 - 소규모 RLHF 구현  
 - 교육용 LLM 훈련  
url: https://github.com/hyunwoongko/nanoRLHF  
---  
이 프로젝트는 PyTorch와 Triton을 제외한 모든 핵심 구성 요소를 처음부터 수동으로 구현하여 RLHF(강화학습 기반 인간 피드백) 훈련을 교육 목적으로 구현한 것입니다. 대규모 시스템의 명료성과 핵심 개념을 중점으로 한 최소한의 모듈들(SFT, RL 훈련 파이프라인, 평가 포함)로 구성되어 있으며, 오픈소스 수학 데이터셋으로 소형 Qwen3 모델을 훈련시키는 것을 목표로 합니다. 분산 컴퓨팅, 3D 병렬화, 효율적인 추론 엔진 등 대규모 모델 훈련의 핵심 메커니즘을 이해하는 데 도움을 줍니다.