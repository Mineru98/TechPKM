---
Language: Python
tags:
 - 언어모델
 - 스파스활성화
 - LLM
 - 성능최적화
 - 오픈소스
aliases:
 - Bamboo-7B
 - Bamboo-v0.1
 - 스파스LLM
url: https://github.com/SJTU-IPADS/Bamboo
---
Bamboo-v0.1은 높은 희소성(스파시티)을 유지하면서 Mistral-7B와 동등한 성능을 제공하는 70억 파라미터 규모의 언어 모델입니다. 이 모델은 활성화 뉴런 임계값 선택을 통해 다양한 희소성 수준(100%~10%)에서도 안정적인 성능(PPL 6.484~6.524)을 보이며, PowerInfer 및 llama.cpp 환경에서 효율적인 추론이 가능합니다. 주요 벤치마크에서 평균 57.1%의 성능을 기록하며, 특히 GSM8K에서 52.84%의 정확도를 달성했습니다. 현재 영어 데이터셋 기반 훈련 모델로 상용 및 학술 연구에 자유롭게 사용할 수 있습니다.