---
Language: Python, C++, Swift, Kotlin
tags:
 - 온디바이스 AI
 - 모델 최적화
 - PyTorch
 - 에지 컴퓨팅
 - 하드웨어 백엔드
aliases:
 - ExecuTorch
 - PyTorch 배포
 - 온디바이스 추론
 - 에지 AI
url: https://github.com/pytorch/executorch
---
**ExecuTorch**는 PyTorch로 개발된 AI 모델을 스마트폰부터 마이크로컨트롤러까지 다양한 장치에 배포하기 위한 통합 솔루션입니다. Meta의 Instagram, WhatsApp, Quest 3 등 실제 서비스에 적용된 기술로, LLM, 비전, 음성, 멀티모달 모델을 PyTorch API로 직접 내보내고 최적화하는 기능을 제공합니다. ONNX/TFLite 변환 없이 하드웨어별 가속(백엔드)을 지원하며, 50KB 미만의 경량 런타임으로 리소스 제약이 있는 환경에서도 실행 가능합니다. 12개 이상의 하드웨어 백엔드(Qualcomm, ARM, Apple 등)와 통합되어 유연한 배포가 가능합니다.