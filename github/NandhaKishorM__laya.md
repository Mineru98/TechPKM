---
Language: Python
tags:
 - 비자율회귀
 - 강화학습
 - 다국어NLP
 - 의사결정엔진
 - PyTorch
aliases:
 - Laya
 - laya decision engine
 - RLCD
url: https://github.com/NandhaKishorM/laya
---
Laya는 100개 이상의 언어에 대해 단일 순전파(약 33ms)로 타입화된 결정(choice, score, noul)을 수행하는 다국어 비자율회귀(non-autoregressive) 의사결정 엔진입니다. RLCD(엄격하게 proper한 스코어링 규칙을 이용한 강화학습)로 학습되어 통계적으로 의미 있는 신뢰도 점수를 제공하며, 요청별로 최적의 체크포인트(laya, laya-multilingual, laya-typed-decisions)를 선택하는 라우터를 내장하고 있습니다. 서포트 티켓 분류, 모델 라우팅, 프롬프트 가드레일, 콘텐츠 안전 검토 등의 워크플로우 프리셋을 제공하며, 도메인 데이터로 파인튜닝하여 최고의 성능을 발휘하도록 설계되었습니다.