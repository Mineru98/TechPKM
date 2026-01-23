---
Language: Python  
tags:  
 - RLHF  
 - 분산학습  
 - LLM  
 - Triton  
 - 교육용  
aliases:  
 - nanoRLHF  
 - 초소형 RLHF  
 - 분산 학습 프레임워크  
url: https://github.com/hyunwoongko/nanoRLHF  
---  
이 프로젝트는 PyTorch와 Triton을 제외한 모든 핵심 구성요소를 수동으로 구현하여 RLHF(강화학습 기반 인간 피드백) 훈련을 처음부터 수행하는 것을 목표로 합니다. 8개의 H200 GPU를 사용해 SFT(지도 미세 조정) 및 RL 훈련 파이프라인을 포함하며, 오픈소스 수학 데이터셋으로 소규모 Qwen3 모델을 훈련하는 데 중점을 둡니다. 각 모듈은 생산성과 효율성보다는 명확성과 핵심 개념 이해를 위해 설계된 교육용 재구현입니다.  

이 프로젝트는 `nanosets`(제로 복사 데이터셋 라이브러리), `nanoray`(분산 컴퓨팅 엔진), `nanotron`(3D 병렬화 엔진), `kernels`(커스텀 Triton 커널), `nanovllm`(고속 추론 엔진), `nanoverl`(RLHF 훈련 프레임워크)로 구성되어 있으며, 최종적으로 전체 RLHF 파이프라인을 실행할 수 있습니다. Apache 2.0 라이선스로 배포됩니다.