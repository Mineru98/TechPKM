---
Language: Python
tags:
 - BPE
 - 토크나이저
 - 자연어처리
 - 파이썬
 - 토크나이저학습
aliases:
 - 미니멀 BPE
 - 간단한 BPE
 - 바이트 페어 인코딩
url: https://github.com/cdince/minbpe
---
이 프로젝트는 대형 언어 모델(LLM)에서 일반적으로 사용되는 바이트 페어 인코딩(BPE) 알고리즘을 구현한 미니멀하고 깔끔한 파이썬 코드입니다. GPT-2 논문 및 OpenAI의 코드 릴리스에서 유명해진 BPE 알고리즘을 기반으로 하며, Llama, Mistral을 포함한 모든 현대 LLM에서 토크나이저 학습에 사용됩니다. 기본 토크나이저(BasicTokenizer)와 정규 표현식을 사용한 토크나이저(RegexTokenizer) 두 가지 구현을 제공하며, 특수 토큰 처리와 토크나이저 저장/로드 기능을 지원합니다. 교육용으로도 적합하며, 코드 가독성과 확장성이 강점입니다. 테스트 케이스와 연습 문제도 함께 제공됩니다.