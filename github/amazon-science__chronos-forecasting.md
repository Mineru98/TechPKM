---
Language: Python
tags:
 - 시계열 예측
 - HuggingFace
 - 사전훈련 모델
 - AWS SageMaker
 - Chronos
aliases:
 - Chronos-2
 - Chronos-Bolt
 - Chronos 예측 모델
 - 시계열 예측 모델
url: https://github.com/amazon-science/chronos-forecasting
---
Chronos는 Amazon Science에서 개발한 시계열 예측을 위한 사전훈련 모델 패밀리입니다. Chronos-2, Chronos-Bolt, Chronos로 구성되며, 단변량/다변량 예측과 외생 변수 통합이 가능한 제로샷 예측 기능을 제공합니다. HuggingFace를 통해 다양한 사전훈련 모델을 지원하며, AWS SageMaker와 연동해 빠른 배포가 가능합니다. 

---

### 주요 특징
- **Chronos-2**: 다변량 및 외생 변수 지원 제로샷 예측, 최신 벤치마크에서 최고 성능
- **Chronos-Bolt**: 동일 규모 대비 250배 빠른 추론 속도, 20배 메모리 효율성
- **HuggingFace 통합**: 데이터셋 및 모델 라이브러리에서 바로 사용 가능
- **AWS SageMaker 지원**: 실시간 추론, 서버리스 엔드포인트 배포 기능 제공

### 적용 분야
- 에너지 수요 예측, 금융 시계열 분석, 물류 수요 계획 등 다양한 도메인에서 활용 가능
- 외생 변수(날씨, 이벤트 등)를 고려한 정교한 예측이 필요한 시나리오에 최적화됨