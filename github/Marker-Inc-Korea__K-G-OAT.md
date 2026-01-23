---
Language: Python  
tags:  
 - 한국어_LLM  
 - IA3_파인튜닝  
 - Fewshot_평가  
 - KoAlpaca  
 - 폴리글롯_모델  
aliases:  
 - KGOAT  
 - K(G)OAT  
 - IA3_적응형_어댑터  
 - 마커_미디어그룹_컨소시엄  
url: https://github.com/Marker-Inc-Korea/K-G-OAT  
---  
K(G)OAT는 IA3(Infused Adapter by Inhibiting and Amplifying Inner Activations) 방식으로 파인튜닝된 한국어 LLM(소규모 매개변수 모델)입니다. 기존 LoRA 방식 대비 더 적은 파라미터(802,816개)로도 폴리글롯-5.8b 및 ko-Alpaca-5.8b 대비 우수한 성능(프롬프트1 기준 0.712, 프롬프트2 기준 0.810)을 달성했으며, NSMC 데이터셋 기반 Fewshot 평가에서 검증되었습니다. KoAlpaca v1.1 데이터셋과 수정된 프롬프트("질문: ...\n정답: ...")를 활용해 훈련되었으며, A5000 GPU 2대에서 학습되었습니다.  

IA3는 기존 LoRA와 달리 어텐션 스코어 재조정 방식을 통해 추론 시간 단축(1.7초)과 메모리 효율성을 동시에 개선한 방법론으로, 한국어 NLP 태스크에서 높은 활용 가능성을 입증했습니다. 연구는 마커와 미디어그룹사람과숲 컨소시엄의 지원으로 수행되었으며 MIT 라이선스로 공개되었습니다.