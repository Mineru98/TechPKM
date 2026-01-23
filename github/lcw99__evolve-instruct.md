---
Language: Python
tags:
 - 한국어 LLM
 - 데이터셋 생성
 - 인스트럭트 튜닝
 - WizardLM
 - 다국어 지원
aliases:
 - evolve-instruct
 - 한국어 인스트럭션 데이터셋
 - LLM 훈련 데이터
url: https://github.com/lcw99/evolve-instruct
---
이 프로젝트는 영어 기반 LLM 인스트럭션을 한국어로 변환하는 데이터셋 생성 코드입니다. h2o-wizardlm과 WizardLM 논문을 기반으로 하며, ChatGPT를 활용해 36,000개 이상의 Q&A 페어를 생성했습니다. 생성된 데이터셋은 한국어 LLM(예: polyglot-ko-12.8b-chang-instruct-chat) 훈련에 사용되며, FastChat 등의 프레임워크에서 활용 가능합니다.