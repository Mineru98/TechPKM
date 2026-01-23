---
Language: Python
tags:
 - 딥러닝
 - JAX
 - 대규모모델
 - 분산학습
 - Apple
aliases:
 - AXLearn
 - Apple AXLearn
 - 대규모 딥러닝 라이브러리
 - AXLearn 딥러닝
url: https://github.com/apple/axlearn
---
AXLearn은 대규모 딥 러닝 모델 개발을 지원하기 위해 JAX와 XLA 위에 구축된 라이브러리입니다. Apple에서 개발되었으며, 재사용 가능한 구성 요소를 조합하여 모델을 구축하고 Flax, Hugging Face Transformers와 같은 다른 라이브러리와 통합할 수 있는 객체 지향적 접근 방식을 채택했습니다. 이 라이브러리는 수천 개의 가속기에서 높은 활용률로 수조 개의 매개변수를 가진 모델을 훈련시킬 수 있도록 확장성을 갖추었으며, 자연어 처리, 컴퓨터 비전, 음성 인식 등 다양한 분야를 지원합니다. GSPMD 기반의 글로벌 계산 패러다임을 통해 가상 글로벌 컴퓨터에서의 계산을 기술할 수 있도록 설계되었습니다.