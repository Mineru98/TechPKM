---
Language: Python/C++/CUDA  
tags:  
 - 언어모델 최적화  
 - BERT  
 - 고속추론  
 - 트랜스포머  
 - 딥러닝 벤치마크  
aliases:  
 - UltraFastBERT  
 - FFF 추론  
 - 초고속 BERT  
 - crammedBERT 확장  
url: https://github.com/pbelcak/UltraFastBERT  
---  
UltraFastBERT는 기존 BERT 대비 지수적으로 빠른 추론을 위한 언어 모델 구현체입니다. 논문 "Exponentially Faster Language Modelling"을 기반으로 FFF(Fast Feed Forward) 레이어를 도입하여 계산 효율성을 개선하였으며, CPU/GPU 환경에서 벤치마크 성능을 검증했습니다. 허깅페이스에서 사전 학습된 모델을 제공하며, 훈련/미세조정/추론용 코드를 포함하고 있습니다.  

핵심 기술 스택은 Python, C++, CUDA이며, 트랜스포머 기반 모델의 가속화 연구에 활용할 수 있습니다. 벤치마크 결과 재현을 위한 CPU/파이토치/CUDA 구현체도 함께 제공됩니다.