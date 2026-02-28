---
Language: Python
tags:
 - LoRA
 - Fine-tuning
 - SakanaAI
 - LLM
 - Adapter
aliases:
 - Text-to-LoRA
 - T2L
url: https://github.com/SakanaAI/text-to-lora
---
SakanaAI에서 개발한 Text-to-LoRA(T2L)는 텍스트로 설명된 작업 설명(Task Description)을 통해 트랜스포머 모델을 즉시 적응(Adapt)시키는 방법론입니다. 이 프로젝트는 미리 학습된 T2L 모델을 사용하여 수학적 추론 등 다양한 작업에 맞춤형 LoRA 어댑터를 즉시 생성하고, 생성된 LoRA를 평가할 수 있는 파이프라인을 제공합니다. 또한, 모델을 직접 학습(SFT, Reconstruction)시키기 위한 스크립트와 웹 인터페이스 데모를 포함하고 있습니다.