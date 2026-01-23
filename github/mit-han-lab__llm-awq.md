---
Language: Python
tags:
 - LLM 압축
 - 양자화 기술
 - 엣지 디바이스 최적화
 - PyTorch
 - 멀티모달 모델
aliases:
 - AWQ
 - Activation-aware Weight Quantization
 - LLM 양자화
 - TinyChat
url: https://github.com/mit-han-lab/llm-awq
---
AWQ는 대규모 언어 모델의 효율적인 압축과 가속을 위한 활성화 인식 가중치 양자화 기술입니다. INT3/4 비트 수준의 양자화를 지원하며, 명령어 튜닝 모델과 멀티모달 언어 모델(VILA, LLaVA 등)에 적용 가능합니다. 엣지 디바이스에서 리소스 제약 환경에서도 LLM/VLM 추론을 최적화하여 메모리 사용량을 줄이고 토큰 생성 속도를 향상시킵니다. Hugging Face 및 TensorRT-LLM 등과 통합되어 있으며, TinyChat을 통해 클라우드 및 엣지 GPU에서의 효율적인 추론이 가능합니다.