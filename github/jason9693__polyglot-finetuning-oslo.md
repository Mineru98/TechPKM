---
Language: Python  
tags:  
 - 분산학습  
 - OSLO  
 - TensorParallel  
 - Polyglot-ko  
 - KorQuADv1  
aliases:  
 - OSLO 분산 학습 예제  
 - Polyglot-ko 멀티노드 학습  
 - OSLO TensorParallel 튜토리얼  
url: https://github.com/jason9693/polyglot-finetuning-oslo  
---  
이 프로젝트는 OSLO 라이브러리의 TensorParallel 기능을 활용해 EleutherAI Polyglot-ko 1.3B 모델을 KorQuADv1 데이터셋으로 분산 학습하는 방법을 보여주는 예제입니다. 싱글노드(4GPU) 및 멀티노드(8GPU) 환경에서의 학습 실행 방법을 제공하며, 모델 분할과 병렬 처리 구현에 중점을 둡니다. OSLO 설치 및 분산 학습 구성 정보를 포함합니다.