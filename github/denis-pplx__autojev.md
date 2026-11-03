---
Language: Python
tags:
 - 멀티모달
 - LLM
 - 의사결정모델
 - fine-tuning
 - Qwen
aliases:
 - AutoJev
 - AutoJev-27B
 - 오토제브
url: https://github.com/denis-pplx/autojev
---
AutoJev-27B는 Qwen3.8-27B 기반의 멀티모달 의사결정 모델로, 질문당 단일 forward pass로 선택지에 대한 확률을 반환합니다. 자율 에이전트를 활용해 연구, 데이터 생성, 학습, 평가, 배포까지 수행했으며, TypeSafe 호환 API와 브라우저 플레이그라운드를 제공합니다. 베이스 모델 대비 정확도와 보정(calibration) 지표에서 큰 폭의 성능 향상을 보였습니다.