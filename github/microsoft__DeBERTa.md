---
Language: Python  
tags:  
 - 자연어 처리  
 - 딥러닝  
 - 트랜스포머 모델  
 - 사전 훈련 모델  
 - BERT 변형  
aliases:  
 - DeBERTa  
 - 디버타  
 - 디버타V3  
 - ELECTRA 스타일 사전 훈련  
url: https://github.com/microsoft/DeBERTa  
---  
DeBERTa는 BERT 및 RoBERTa 모델을 향상시키기 위해 **분리된 어텐션 메커니즘**과 **강화된 마스크 디코더**를 도입한 트랜스포머 기반 자연어 처리 모델입니다. 분리된 어텐션은 토큰의 콘텐츠와 위치 정보를 독립적으로 처리하며, 마스크 디코더는 사전 훈련 시 토큰 예측 정확도를 개선합니다. 이 저장소는 DeBERTa와 DeBERTa V3의 공식 구현체를 포함하며, GLUE, SuperGLUE, SQuAD 등 다양한 벤치마크에서 SOTA 성능을 달성했습니다. V3 버전은 ELECTRA 스타일의 목적 함수와 그래디언트 분리 임베딩 공유를 통해 효율성을 추가로 향상시켰습니다.