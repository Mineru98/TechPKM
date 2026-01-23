---
Language: Python  
tags:  
 - 음성 변환  
 - 확산 모델  
 - 딥러닝  
 - 음성 합성  
 - 오픈소스  
aliases:  
 - Diffusion-SVC  
 - 확산 음성 변환  
 - Diffusion-SVC Metadata  
url: https://github.com/CNChTu/Diffusion-SVC  
---  
Diffusion-SVC는 DDSP-SVC 저장소의 확산 모델 부분을 독립적으로 분리한 프로젝트로, 낮은 GPU 메모리 사용량과 빠른 처리 속도를 특징으로 합니다. 이 프로젝트는 기존 확산 모델 대비 실시간 추론이 가능하며, 얕은 확산(Shallow Diffusion)과 Naive 모델 조합을 통해 고품질 변환을 효율적으로 달성할 수 있습니다. 콘텐츠 인코더(ContentVec, Hubert 등)와 호환되며, 사전 훈련된 모델과의 미세 조정(Fine-tuning)을 통해 소규모 데이터셋에서도 우수한 성능을 제공합니다. 음성 변환, 화자 분리, 음질 개선 등 다양한 응용 분야에 활용될 수 있습니다.