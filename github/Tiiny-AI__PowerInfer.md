---
Language: C++
tags:
 - LLM
 - Inference Engine
 - GPU
 - CPU-GPU Hybrid
 - Sparse Model
aliases:
 - PowerInfer
 - 라마엘엘엠
 - LLM 추론 엔진
url: https://github.com/Tiiny-AI/PowerInfer
---

PowerInfer는 LLM 추론 과정에서 나타나는 뉴런 활성화의 국지성(activation locality)을 활용하여, 소비자용 GPU 환경에서도 서버급 수준의 고속 추론을 가능하게 하는 엔진입니다. 핫 뉴런(hot neurons)은 GPU에 상주시키고 콜드 뉴런(cold neurons)은 CPU에서 계산하는 하이브리드 설계 방식을 통해 메모리 요구량을 최소화하고 처리 속도를 획기적으로 개선했습니다. 특히 ReLU 기반의 희소 모델(Sparse Model)을 지원하여, llama.cpp 대비 최대 11배 이상의 성능 향상을 달성합니다.