---
Language: Python
tags:
 - 분산추론서빙
 - Kubernetes
 - vLLM
 - LLM
 - 고성능추론
aliases:
 - llm-d
 - LLM-D
 - 분산추론최적화
 - 분산모델서빙
url: https://github.com/llm-d/llm-d
---
llm-d는 다양한 가속기에서 최첨단(SOTA) 추론 성능을 달성하기 위한 쿠버네티스 기반 분산 추론 서빙 스택입니다. 주요 오픈소스 모델들을 NVIDIA GPU, AMD GPU, Google TPU, Intel XPU 등 다양한 하드웨어 가속기와 인프라 제공업체에서 확장 가능하게 서빙할 수 있도록 지원합니다. 지능형 추론 스케줄링, 프리필/디코드 분리, 와이드 전문가 병렬화 등 테스트되고 벤치마크된 배포 경로를 제공하며, vLLM, Inference Gateway, Kubernetes와 같은 오픈소스 컴포넌트를 통합하여 대규모 서빙의 복잡성을 해결합니다.