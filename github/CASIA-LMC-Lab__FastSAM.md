---
Language: Python
tags:
 - 객체 분할
 - 실시간 세그멘테이션
 - YOLOv8
 - CNN 모델
 - 이미지 처리
aliases:
 - FastSAM
 - Fast Segment Anything Model
 - CNN 기반 세그멘테이션
 - 초고속 객체 분할
url: https://github.com/CASIA-IVA-Lab/FastSAM
---
**Fast Segment Anything Model(FastSAM)**은 SAM 모델과 유사한 성능을 유지하면서 50배 빠른 처리 속도를 제공하는 CNN 기반 세그멘테이션 모델입니다. SA-1B 데이터셋의 2%만 사용해 훈련되었으며, 다양한 프롬프트 모드(텍스트, 박스, 점)와 "Everything 모드"를 지원합니다. 실시간 성능이 필요한 애플리케이션에 최적화되어 있으며, 객체 분할, 이상 탐지, 건물 추출 등 다양한 다운스트림 작업에 활용될 수 있습니다.  

FastSAM은 YOLOv8 아키텍처를 기반으로 하며, PyTorch와 TorchVision 환경에서 구동됩니다. HuggingFace, Colab, Replicate 등에서 데모를 체험할 수 있고, Gradio 기반의 웹 인터페이스도 제공됩니다. Apache 2.0 라이선스로 배포됩니다.