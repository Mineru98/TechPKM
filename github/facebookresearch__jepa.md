---
Language: Python  
tags:  
 - 자기지도학습  
 - 비디오 표현 학습  
 - ViT-H  
 - ViT-L  
 - PyTorch  
aliases:  
 - V-JEPA  
 - Video Joint Embedding Predictive Architecture  
 - 메타 AI 비디오 모델  
url: https://github.com/facebookresearch/jepa  
---  
V-JEPA는 비디오 데이터에서 시각적 표현을 학습하기 위한 자기지도학습 방법으로, 비디오 픽셀 관찰을 통해 다양한 다운스트림 작업에 적용 가능한 표현을 생성합니다. 이 모델은 사전 훈련된 인코더와 예측기 네트워크를 사용하며, 비디오의 마스킹된 영역에 대한 예측 능력을 통해 시공간적 일관성을 보입니다. PyTorch 기반의 오픈소스 구현체로, VideoMix2M 데이터셋으로 학습되며 이미지 분류 및 비디오 분류 작업에서 높은 성능을 달성합니다.