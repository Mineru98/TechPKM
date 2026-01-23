---
Language: Python
tags:
 - LLM quantization
 - GPTQ 알고리즘
 - 모델 압축
 - PyTorch
 - HuggingFace
aliases:
 - AutoGPTQ
 - GPTQModel
 - 모델 양자화
 - LLM 최적화
 - GPTQ 통합
url: https://github.com/PanQiWei/AutoGPTQ
---
AutoGPTQ는 GPTQ 알고리즘 기반의 사용하기 쉬운 LLM 양자화 패키지로, 사용자 친화적인 API를 제공합니다. 이 프로젝트는 대형 언어 모델을 4비트 또는 3비트로 양자화하여 메모리 사용량을 줄이고 추론 속도를 개선하는 데 중점을 둡니다. HuggingFace Transformers, Optimum, PEFT와의 통합이 가능하며, 다양한 모델과 하드웨어 아키텍처를 지원합니다. 주요 기능으로는 양자화, 추론, 모델 푸시/풀, Marlin 및 Exllama 커널 지원이 포함됩니다. 현재 유지보수 중단되었으며, 대안 프로젝트로 GPTQModel을 추천합니다.