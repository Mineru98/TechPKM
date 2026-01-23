---
Language: Python  
tags:  
 - 기계번역  
 - LLM  
 - 파인튜닝  
aliases:  
 - ALMA 번역 모델  
 - ALMA-R  
url: https://github.com/qwopqwop200/ALMA-en2ko  
---
**ALMA**는 대규모 언어 모델(LLM) 기반의 다국어 번역 모델로, 단방향 데이터 파인튜닝과 고품질 병렬 데이터 최적화를 결합한 2단계 학습 방식을 채택하여 뛰어난 번역 성능을 구현합니다. ALMA-R은 LoRA 파인튜닝과 대비 선호도 최적화(CPO)를 적용해 GPT-4 수준의 정확도를 달성하며, 영어↔독일어, 영어↔체코어 등 10개 언어 쌍을 지원합니다. HuggingFace에서 모델 체크포인트와 데이터셋을 제공하며, AMD/엔비디아 GPU 환경에서 사용 가능합니다.  

핵심 기능:  
- 단방향/병렬 데이터 파인튜닝 및 LoRA 지원  
- 대비 선호도 최적화(CPO)를 통한 성능 향상  
- LLaMA-2, OPT 등 다양한 기반 모델 호환  
- WMT 벤치마크에서의 경쟁력 있는 성능  
- 다중 GPU 평가 지원  

![ALMA 번역 흐름도](almar.png)