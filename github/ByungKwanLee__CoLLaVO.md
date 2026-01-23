---
Language: Python  
tags:  
 - Vision-Language Model  
 - Zero-Shot Learning  
 - Multimodal AI  
 - Computer Vision  
 - Large Language Model  
aliases:  
 - CoLLaVO  
 - 크레용 언어-시각 모델  
 - Crayon Large Language and Vision mOdel  
url: https://github.com/ByungKwanLee/CoLLaVO  
---  
CoLLaVO는 객체 수준의 이미지 이해 능력을 향상시키기 위해 설계된 대규모 언어-시각 통합 모델입니다. 크레용 프롬프트(Crayon Prompt) 기반의 시각적 프롬프트 튜닝과 Dual QLoRA 학습 전략을 활용하여 다양한 제로샷 비전-언어 작업에서 우수한 성능을 달성했습니다. 특히 GPT-4V, Gemini-Pro 등 폐쇄형 모델 대비 MME, POPE, MM-Bench 등 주요 벤치마크에서 월등한 결과를 보여주며, Huggingface를 통해 공개된 7B 파라미터 모델을 제공합니다.  

> 핵심 기술: Panoptic 색상 지도 기반 프롬프트 튜닝, 객체 수준 이해 보존 학습 전략  
> 주요 성능: MME-P 1689.7, POPE 정확도 87.2%, MM-Bench 83.0% (제로샷 기준)