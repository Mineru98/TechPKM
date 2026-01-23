---
Language: Python  
tags:  
 - RLHF  
 - Gradio  
 - 인간 피드백  
 - 선호도 표시  
 - 보상 모델 훈련  
aliases:  
 - LLM-Pref-Mark  
 - 선호도 표시 UI  
 - RLHF 인터페이스  
 - Gradio 선호도 마킹  
url: https://github.com/yourusername/LLM-Pref-Mark-UI  
---  
이 프로젝트는 생성된 텍스트에 대한 인간의 피드백을 선호도로 표시하기 위한 Gradio UI를 제공합니다. 기본 버전(`app.py`)과 고급 버전(`advanced_app.py`)으로 구성되며, RLHF(인간 피드백 강화 학습)를 통한 보상 모델 훈련에 활용될 수 있습니다. 기본 버전은 Flan Alpaca 모델을 데모로 사용하며, 사용자가 모델 교체, 생성 설정 조정, `record()` 함수 구현을 통해 선호도 데이터를 처리할 수 있도록 설계되었습니다. 고급 버전은 UI 기능만 제공하며, Anthropic의 RLHF 연구 논문에서 영감을 받았습니다.