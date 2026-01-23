---
Language: Python  
tags:  
 - PyTorch  
 - 자연어처리  
 - 트랜스포머모델  
 - 사전훈련모델  
 - 파인튜닝  
aliases:  
 - OpenAI-FTLM-PyTorch  
 - 트랜스포머언어모델  
 - OpenAI 언어모델 구현  
 - ROCStories 파인튜닝  
url: https://github.com/openai/finetune-transformer-lm  
---  
이 프로젝트는 OpenAI의 "Improving Language Understanding by Generative Pre-Training" 논문에서 소개된 트랜스포머 언어 모델을 PyTorch로 구현한 것입니다. TensorFlow로 사전 훈련된 가중치를 PyTorch 모델에 로드할 수 있으며, 분류 작업에 파인튜닝하는 기능도 지원합니다. 주요 구성 요소로는 모델 클래스, 가중치 로딩 스크립트, Adam 최적화 알고리즘 수정이 포함되어 있습니다. ROCStories 데이터셋에서 85.84% 정확도를 달성했으며, 단일 GPU(K80)에서 3에폭 훈련 시 약 10분이 소요됩니다.  

> 핵심 기능: OpenAI 사전훈련 모델 변환, 트랜스포머 언어 모델링, 분류 헤드 지원, ROCStories 벤치마크 재현  

> 기술 스택: PyTorch 0.4+, tqdm, scikit-learn, spaCy, pandas  
> 주요 의존성: TensorFlow 사전훈련 가중치 호환성  
> 벤치마크: 기존 TensorFlow 구현(85.8%)과 유사한 성능 달성