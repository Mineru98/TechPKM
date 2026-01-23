---
Language: Python
tags:
 - 한국어_LLM
 - 데이터셋_생성
 - 인스트럭션_튜닝
 - WizardLM
 - 다국어_지원
aliases:
 - evolve-instruct
 - 한국어_튜닝_데이터셋
 - WizardLM_한국어_생성
url: https://github.com/h2oai/h2o-wizardlm
---
이 프로젝트는 영어 기반 LLM 인스트럭션을 한국어 등 다양한 언어로 변환하는 오픈소스 구현체입니다. [h2o-wizardlm]과 [WizardLM] 논문 방법론을 기반으로 10,000개의 한국어 Q&A 쌍과 26,000개의 Alpaca 데이터를 활용해 생성되었으며, 생성된 데이터셋은 한국어 모델 [polyglot-ko-12.8b-chang-instruct-chat] 훈련에 사용되었습니다. FastChat 등 주요 LLM 프레임워크에서 활용 가능한 한국어 특화 인스트럭션 튜닝 데이터셋입니다.