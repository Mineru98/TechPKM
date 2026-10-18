---
Language: Python
tags:
 - 이미지-분할
 - Background-Removal
 - Deep-Learning
 - Computer-Vision
 - 디투모스-이미지-세그멘테이션
aliases:
 - BiRefNet
 - Bilateral Reference
 - 고해상도 이미지 분할
 - BiRefNet-matting
url: https://github.com/ZhengPeng7/BiRefNet
---
BiRefNet은 고해상도 이분법 이미지 분할(Dichotomous Image Segmentation)을 위한 SOTA 딥러닝 모델로, 양측 참조(Bilateral Reference) 구조를 활용해 DIS, COD, HRSOD 등 다양한 분할 작업에서 최고 성능을 달성했습니다. Hugging Face에서 한 줄 코드로 모델을 로드할 수 있으며, 배경 제거, 매팅(matting), 박스 가이드 분할 등 실용적인 용도로 확장된 다양한 사전 학습 가중치를 제공합니다. ONNX, TensorRT 변환 및 커스텀 데이터 파인튜닝 기능도 지원합니다.