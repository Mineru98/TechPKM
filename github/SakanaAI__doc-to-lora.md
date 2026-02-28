---
Language: Python
tags:
 - MachineLearning
 - LLM
 - LoRA
 - SakanaAI
 - RAG
aliases:
 - Doc-to-LoRA
 - D2L
 - 문서 내부화 학습
url: https://github.com/SakanaAI/doc-to-lora
---
Doc-to-LoRA(D2L)는 문서 컨텍스트를 즉시 내부화하여 LLM의 파라미터에 반영할 수 있도록 학습하는 Sakana AI의 프로젝트입니다. 하이퍼네트워크(Hypernetwork)를 통해 입력 텍스트를 LoRA 가중치로 변환하며, 별도의 프롬프트 엔지니어링 없이 모델이 주어진 정보를 기반으로 정확하게 답변할 수 있도록 돕습니다. 긴 문서를 효율적으로 처리하고 모델의 환각(Hallucination) 현상을 줄이는 것을 목표로 하며, Python API를 통해 제공됩니다.