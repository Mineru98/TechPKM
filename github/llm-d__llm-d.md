---
Language: Go, Python, JavaScript
tags:
 - 분산 추론 서빙
 - Kubernetes 네이티브
 - vLLM
 - LLM 최적화
 - 하드웨어 가속기
aliases:
 - llm-d
 - 분산 추론 스택
 - SOTA 추론 성능
url: https://github.com/llm-d/llm-d
---
llm-d는 모든 가속기에서 최첨단(SOTA) 추론 성능을 달성하기 위한 쿠버네티스 네이티브 분산 추론 서빙 스택입니다. 주요 OSS 모델(예: Llama-70B, DeepSeek-R1)을 다양한 하드웨어 가속기(NVIDIA GPU, AMD GPU, Google TPU, Intel XPU) 및 인프라 환경에서 확장할 수 있도록 지원합니다. vLLM, Inference Gateway, 쿠버네티스 등을 기반으로 하며, 추론 스케줄링, 프리필/디코드 분리, MoE 모델 최적화 등 검증된 레시피를 제공하여 생산 배포를 가속화합니다. 주요 기능은 지능형 추론 스케줄러, 프리픽스 캐시 계층화, 트래픽/하드웨어 인식 자동 확장 등입니다.