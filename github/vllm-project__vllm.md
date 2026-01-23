---
Language: Python
tags:
 - LLM 서빙
 - 고성능 추론
 - 분산 추론
 - PagedAttention
 - HuggingFace 통합
aliases:
 - vLLM
 - PagedAttention
 - LLM 서빙 프레임워크
 - 분산형 LLM 추론
url: https://github.com/vllm-project/vllm
---
vLLM은 대규모 언어 모델(LLM)의 추론 및 서빙을 위한 빠르고 사용하기 쉬운 라이브러리입니다. UC 버클리에서 시작되어 학계와 산업계의 협력으로 발전한 이 프로젝트는 최첨단 서빙 처리량, 메모리 효율적인 PagedAttention, 연속 배치 처리 등을 통해 고성능 LLM 추론을 제공합니다. HuggingFace 모델과의 원활한 통합, 다양한 디코딩 알고리즘 지원, OpenAI 호환 API 서버 등을 통해 유연성과 사용 편의성을 갖추었으며, NVIDIA GPU부터 TPU까지 다양한 하드웨어 플랫폼을 지원합니다. 주요 특징으로는 양자화(GPTQ/AWQ), FlashAttention/FlashInfer 통합, 추론 병렬화, 스트리밍 출력 등이 있습니다.