---
Language: Python  
tags:  
 - 언어모델  
 - BERT  
 - 제한된컴퓨팅  
 - 스케일링법칙  
 - 단일GPU  
aliases:  
 - Cramming-BERT  
 - 단일GPU언어모델  
 - 제한된자원BERT  
 - CrammingLM  
 - 소규모트레인링  
url: https://github.com/JonasGeiping/cramming/blob/main/README.md  
---  
이 프로젝트는 단일 GPU에서 24시간 내 BERT 기반 언어 모델을 처음부터 훈련시키는 "크램밍" 기법을 연구합니다. 제한된 컴퓨팅 자원으로도 대규모 모델의 스케일링 법칙을 따르며 GLUE 벤치마크에서 경쟁력 있는 성능을 달성하는 방법을 탐구합니다. PyTorch 2.0을 기반으로 한 훈련 파이프라인과 데이터 전처리 최적화를 포함하며, Hugging Face를 통해 사전 처리된 데이터셋과 체크포인트를 제공합니다.  

주요 기여로는 기존 훈련 파이프라인 재구성, 소규모 설정에서의 성능 개선 요소 분석, 그리고 컴퓨팅 제약 환경에서의 실용적인 적용 가능성을 입증합니다.