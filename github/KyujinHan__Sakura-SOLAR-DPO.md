---
Language: Python  
tags:  
 - LLM 최적화  
 - DPO 훈련  
 - 오픈소스 모델  
aliases:  
 - Sakura-SOLAR-DPO  
 - Sakura 모델 훈련  
 - DPO 기반 LLM  
url: https://github.com/KyujinHan/Sakura-SOLAR-DPO  
---  
Sakura-SOLAR-DPO 프로젝트는 (주)미디어그룹사람과숲과 (주)마커의 LLM 연구 컨소시엄에서 개발된 오픈소스 대형언어모델(LLM) 훈련 저장소입니다. 2023년 12월 기준 Open LLM 리더보드 1위를 기록한 `Sakura-SOLAR-Instruct` 모델의 훈련 코드와 하이퍼파라미터, LoRA 기반 DPO(직접선호최적화) 기법을 공유하는 것이 주목적입니다. 모델 병합(mergekit)과 DPO 학습 파이프라인을 제공하며, 수학/일반 도메인 최적화를 위한 다양한 변형 모델을 포함합니다.  

> 📌 핵심 특징:  
> - **SLERP 병합 기법**과 **LoRA 미세조정**을 활용한 모델 최적화  
> - 수학/일반 성능 균형을 위한 다중 변형 모델 제공  
> - 오픈소스 생태계를 위한 하이퍼파라미터 및 데이터셋 공유