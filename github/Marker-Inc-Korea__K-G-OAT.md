---
Language: Python  
tags:  
 - 한국어-LLM  
 - IA3-fine-tuning  
 - Fewshot-Learning  
 - 자연어처리  
 - 파라미터-효율성  
aliases:  
 - KGOAT  
 - K(G)OAT  
 - IA3-한국어모델  
 - 경량화-LLM  
url: https://github.com/Marker-Inc-Korea/K-G-OAT  
---  
**K(G)OAT**는 (주)마커와 (주)미디어그룹사람과숲 컨소시엄에서 개발된 한국어 LLM 모델로, **IA3(T-Few) 방식**을 적용해 기존 LoRA 대비 **적은 파라미터(802,816개)**로 효율적인 미세조정을 구현했습니다. KoAlpaca와 Polyglot-5.8b를 베이스로 훈련되었으며, NSMC 데이터셋 기반 Fewshot 평가에서 **프롬프트1 기준 0.712**, **프롬프트2 기준 0.810**의 정확도를 달성했습니다. 특히 IA3는 Attention 레이어의 rescale 기법을 통해 추론 시간(1.7초)과 성능을 동시에 개선했으며, A5000 GPU 2장으로 훈련된 점이 특징입니다. HuggingFace에 모델 가중치와 평가 코드가 공개되어 있습니다.