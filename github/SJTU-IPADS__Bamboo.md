---
Language: Python
tags:
 - 대규모 언어 모델
 - 희소 활성화
 - LLM 최적화
 - 모델 효율성
 - 비교 평가
aliases:
 - Bamboo-모델
 - Bamboo-v0.1
 - SJTU-IPADS-Bamboo
url: https://github.com/SJTU-IPADS/Bamboo
---
Bamboo-v0.1은 높은 희소성을 유지하면서도 Mistral-7B와 동등한 성능을 제공하는 7B 대규모 언어 모델입니다. 이 모델은 활성화 뉴런 임계값 기법을 통해 10% 희소도에서도 6.524의 PPL을 달성하며, 다양한 벤치마크에서 평균 57.1% 정확도를 보입니다. PowerInfer 및 llama.cpp 프레임워크에서 CPU/GPU 하이브리드 환경에서 최대 4.38배 빠른 추론 속도를 제공하며, Apache-2.0 라이선스 하에 학술적 및 상업적 사용이 가능합니다. 주요 특징으로는 희소 활성화 메커니즘, 다중 하드웨어 최적화, 영어 중심의 학습 데이터 활용 등이 있습니다.