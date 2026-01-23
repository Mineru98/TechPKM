---
Language: Python  
tags:  
 - Open-Vocabulary Detection  
 - Real-Time Object Detection  
 - Zero-Shot Learning  
 - YOLO  
 - CVPR2024  
aliases:  
 - YOLO-World  
 - YOLOWorld  
 - YOLO-World-V2  
 - YOLO-World-Image  
 - YOLO-World-Seg  
url: https://github.com/AILab-CVC/YOLO-World  
---  
YOLO-World는 대규모 데이터셋(객체 검출, 그라운딩, 이미지-텍스트 데이터 포함)으로 사전 학습된 차세대 YOLO 객체 검출 모델입니다. 이 모델은 사용자 정의 어휘를 실시간으로 처리할 수 있는 **프롬프트 기반 검출** 방식을 지원하며, 추론 속도 최적화를 위해 어휘 임베딩을 모델 파라미터로 재매개변수화했습니다. CVPR 2024에 채택된 이 프로젝트는 LVIS, COCO 등의 벤치마크에서 뛰어난 제로샷 성능을 입증했으며, 세그멘테이션 확장 버전(YOLO-World-Seg)과 이미지/텍스트 프롬프트 튜닝 기능도 제공합니다. HuggingFace Spaces, Colab, TFLite, ONNX 등 다양한 플랫폼을 통해 배포 및 활용이 가능합니다.  

> 📌 핵심 기능:  
> - **실시간 오픈-보캐불러리 검출**  
> - **재매개변수화(Reparameterization)** 를 통한 추론 효율성 향상  
> - **세그멘테이션 지원** (YOLO-World-Seg)  
> - **이미지/텍스트 프롬프트 튜닝**  
> - 다양한 모델 크기(S/M/L/X) 및 해상도 지원(640~1280)  

> 🚀 배포: HuggingFace, TFLite(INT8 양자화), ONNX, Gradio 데모 등.