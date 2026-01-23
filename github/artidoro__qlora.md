---
Language: Python
tags:
 - LLM
 - 파인튜닝
 - 양자화
 - HuggingFace
 - bitsandbytes
aliases:
 - QLoRA
 - QuantizedLoRA
 - LLM효율성
 - LLM파인튜닝
url: https://github.com/artidoro/qlora/blob/main/README.md
---
QLoRA(Quantized LoRA)는 양자화된 대형 언어 모델(LLM)의 효율적인 파인튜닝을 위한 기술입니다. 4비트 양자화와 LoRA 어댑터를 결합해 단일 48GB GPU에서도 650억 파라미터 모델을 파인튜닝할 수 있으며, 전체 16비트 파인튜닝 성능을 유지합니다. Guanaco 모델 계열은 Vicuna 벤치마크에서 ChatGPT 성능 대비 99.3%를 달성하며, 4비트 훈련 및 다양한 최적화 기법(Double Quantization, Paged Optimizer)을 지원합니다. MIT 라이선스로 공개되었으며 LLaMA 라이선스를 준수합니다.