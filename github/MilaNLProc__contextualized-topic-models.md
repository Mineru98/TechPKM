---
Language: Python
tags:
 - 토픽 모델링
 - 자연어 처리
 - BERT 임베딩
 - 머신러닝
 - Python 라이브러리
aliases:
 - contextualized-topic-models
 - CTM
 - 토픽 모델링 라이브러리
 - BERT 기반 토픽 모델
 - Python 토픽 분석
url: https://github.com/MilaNLProc/contextualized-topic-models
---
Contextualized Topic Models(CTM)는 사전 훈련된 언어 모델(예: BERT)의 임베딩을 활용한 토픽 모델링 라이브러리입니다. CombinedTM과 ZeroShotTM 두 가지 모델을 제공하며, CombinedTM은 BoW와 임베딩을 결합해 일관된 토픽을 생성하고, ZeroShotTM은 학습 데이터에 없는 단어도 처리 가능한 크로스링구얼 지원이 가능합니다. 다중 언어 지원, 전처리 파이프라인, 인간-루프 분류기(Kitty) 기능을 포함하며, SBERT 기반의 임베딩을 유연하게 활용할 수 있습니다.  

**핵심 기능**:  
- BERT 기반 토픽 모델링  
- 크로스링구얼 토픽 분석  
- 전처리 자동화 및 단어 필터링  
- 인간-루프 분류기(Kitty) 통합  
- 다양한 언어 모델 지원(HuggingFace 호환)  

**주요 모델**:  
- **CombinedTM**: BoW + 임베딩 결합으로 일관성 향상  
- **ZeroShotTM**: 제로샷 학습 및 크로스링구얼 지원  
- **Kitty**: 빠른 문서 분류 및 클러스터링  

**사용 사례**:  
- 다국어 토픽 분석  
- 토픽 일관성 개선  
- 문서 필터링 및 분류  
- 임베딩 모델 교체 가능 구조  

MIT 라이선스로 배포되며, 공식 문서 및 Colab 튜토리얼 제공.