---
Language: Python
tags:
 - Qwen
 - 토큰 확률 조정
 - 다국어 생성
 - LLM 편향 감소
 - 모델 수정 도구
aliases:
 - Smoothie-Qwen
 - Qwen 다국어 조정
 - 토큰 스무딩
 - 언어 편향 억제
url: https://github.com/dnotitia/smoothie-qwen
---
**Smoothie Qwen**은 Qwen 및 유사 모델의 토큰 확률을 조정하여 다국어 생성의 균형을 향상시키는 경량 후처리 도구입니다. 유니코드 범위 기반 토큰 식별 및 N-그램 분석을 통해 특정 언어의 과도한 표현을 완화하면서 모델의 핵심 기능을 유지합니다. Hugging Face에 사전 조정된 모델을 제공하여 프로젝트 통합이 용이합니다. 주요 기능은 토큰 가중치 조정, 모델 저장, 다양한 매개변수 지원 등입니다. 실험 결과 95% 이상의 언어 편향 감소 효과를 입증했으며, 코드 생성 등 핵심 성능은 유지됩니다. 추천 설정은 `min_scale = 0.5`, `smoothness = 10.0`입니다.