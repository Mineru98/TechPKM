---
Language: Python  
tags:  
 - 언어모델  
 - BERT  
 - 제한된컴퓨팅  
 - 사전학습  
 - 스케일링  
aliases:  
 - 크램밍BERT  
 - 단일GPU언어모델  
 - 제한된환경언어모델링  
 - 크램밍연구  
 - 소규모BERT  
url: https://github.com/JonasGeiping/cramming  
---  
이 프로젝트는 "Cramming: Training a Language Model on a Single GPU in One Day" 연구를 재현하기 위한 코드를 포함합니다. 제한된 컴퓨팅 자원(단일 GPU, 24시간)으로 BERT형 언어 모델을 처음부터 학습시키며, 소규모 환경에서의 성능 한계와 개선 방안을 분석합니다. 대규모 컴퓨팅 환경에서 관찰된 스케일링 법칙이 제한된 환경에서도 적용되는지를 검증하고, 데이터 처리 및 모델 구조의 최적화 가능성을 탐구합니다. Hugging Face의 사전 처리된 데이터셋을 활용해 효율적인 학습을 지원하며, PyTorch 2.0 이상의 최신 기술을 적용합니다. GLUE 벤치마크를 통해 다운스트림 태스크 성능을 평가합니다.