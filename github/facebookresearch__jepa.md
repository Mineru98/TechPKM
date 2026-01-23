---
Language: Python  
tags:  
 - 비디오 표현 학습  
 - 자기 지도 학습  
 - ViT 모델  
 - 비디오 예측 아키텍처  
 - 메타 AI  
aliases:  
 - V-JEPA  
 - Video Joint Embedding Predictive Architecture  
 - JEPA  
url: https://github.com/facebookresearch/jepa  
---  
V-JEPA는 비디오 픽셀에서 시각적 표현을 학습하기 위한 자기 지도 학습 방법입니다. VideoMix2M 데이터셋을 수동적으로 관찰하여 훈련되며, 모델 파라미터 조정 없이 다양한 다운스트림 작업에서 우수한 성능을 발휘합니다. V-JEPA는 사전 학습된 인코더와 예측기 네트워크를 사용하여 잠재 공간에서의 특징 예측을 수행하며, 생성적 방법과는 달리 픽셀 재구성 없이 작동합니다. 이 프로젝트는 메타 AI 연구소에서 개발되었으며, PyTorch 기반의 공식 코드베이스입니다.