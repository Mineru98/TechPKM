---
Language: Python  
tags:  
 - 멀티모달_LLM  
 - 컴퓨터비전  
 - 참조_그라운딩  
 - 연구_프로젝트  
 - 오픈소스  
aliases:  
 - Ferret_MLLM  
 - Refer_Ground_Anything  
 - Ferret-ICLR2024  
 - MLLM_참조모델  
url: https://github.com/apple/ml-ferret  
---
Ferret은 임의의 형태 참조를 받아들이고 다양한 세분성에서 객체를 정확하게 그라운딩할 수 있는 엔드투엔드 멀티모달 대형 언어 모델(MLLM)입니다. 하이브리드 영역 표현 및 공간 인식 시각 샘플러를 통해 정교한 참조-그라운딩 작업을 수행하며, 대규모 계층적 GRIT 데이터셋과 Ferret-Bench 평가 벤치마크를 포함합니다. 연구는 ICLR 2024에 발표되었으며 학술적 목적으로만 사용이 허가됩니다.  

### 핵심 기능  
- **Ferret 모델**: 세분화된 참조/그라운딩 지원 MLLM  
- **GRIT 데이터셋**: ~1.1M 규모의 계층적 강건 데이터셋  
- **Ferret-Bench**: 참조/그라운딩, 의미론, 지식을 통합 평가하는 벤치마크  
- **Ferret-UI**: UI 중심의 대화형 데모 환경 제공  

> 🔍 주요 기술: LLaMA/Vicuna 기반, LLaVA 코드베이스 활용, 7B/13B 모델 제공  

**사용 제약**: CC BY NC 4.0 라이선스(비상업적 연구 전용)