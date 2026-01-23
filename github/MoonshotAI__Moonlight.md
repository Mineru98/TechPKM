---
Language: Python
tags:
 - LLM 최적화
 - Mixture-of-Experts (MoE)
 - 분산 학습
 - Muon 옵티마이저
 - 대규모 언어 모델
aliases:
 - Moonlight 모델
 - Muon 확장 연구
 - MoE 3B/16B
url: https://github.com/MoonshotAI/Moonlight
---
Moonlight는 Muon 옵티마이저의 확장성을 개선하여 대규모 언어 모델 훈련에 적용한 프로젝트로, 3B/16B 파라미터 규모의 Mixture-of-Expert(MoE) 모델을 5.7T 토큰으로 훈련시켰습니다. 기존 AdamW 대비 약 2배의 계산 효율성을 달성하며, 성능 대비 훈련 FLOPs 측면에서 Pareto 프론티어를 개선했습니다. 메모리 최적화와 통신 효율적인 분산 Muon 구현체를 오픈소스화했으며, 사전 훈련된 모델과 중간 체크포인트를 제공합니다. 주요 기술 기여로는 Muon의 확장성 분석(Weight Decay 적용 및 파라미터별 업데이트 스케일 조정), 분산 구현, 그리고 스케일링 법칙 검증이 포함됩니다.