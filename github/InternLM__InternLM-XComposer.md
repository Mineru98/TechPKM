---
Language: Python  
tags:  
 - 멀티모달 모델  
 - 비전-언어 모델  
 - 오픈소스 AI  
aliases:  
 - InternLM-XComposer-2.5  
 - InternLM-XComposer2.5  
url: https://github.com/InternLM/InternLM-XComposer  
---
InternLM-XComposer-2.5는 텍스트-이미지 이해 및 생성 작업을 위해 설계된 다목적 대형 멀티모달 모델입니다. 7B LLM 백엔드로 GPT-4V 수준의 성능을 제공하며, 24K 인터리빙 이미지-텍스트 컨텍스트로 학습되어 최대 96K의 장문 컨텍스트를 처리할 수 있습니다. 560 × 560 ViT 비전 인코더를 통해 고해상도 이미지를 지원하며, 다중 이미지 대화, 비디오 이해, 웹페이지 제작, 고품질 텍스트-이미지 기사 생성 등 다양한 기능을 제공합니다. 28개 벤치마크에서 기존 오픈소스 모델 대비 우수한 성능을 입증했습니다.  

핵심 기능:  
- 4K HD 해상도 이미지 이해  
- 초장문 컨텍스트(96K) 처리  
- 다중 이미지/비디오 분석  
- 웹페이지 및 문서 자동 생성  
- 30개 이상의 벤치마크에서 SOTA 성능 달성  

Hugging Face와 ModelScope에서 7B/4bit 양자화 모델 제공, LMDeploy를 통한 추론 최적화 지원. 학술 연구 및 상업적 용도 모두 무료 사용 가능.