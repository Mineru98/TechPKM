---
Language: Python  
tags:  
 - 언어 모델 평가  
 - 프롬프트 엔지니어링  
 - 벤치마크  
 - LLM 벤치마크  
aliases:  
 - LMEH  
 - 언어 모델 평가 도구  
 - 오픈 LLM 리더보드  
url: https://github.com/EleutherAI/lm-evaluation-harness  
---  
이 프로젝트는 다양한 언어 모델 평가 작업을 통합하고 표준화된 프레임워크로 제공합니다. 60개 이상의 학술 벤치마크와 수백 가지 하위 작업을 지원하며, HuggingFace, vLLM, OpenAI API 등 다양한 모델 백엔드와 호환됩니다. 오픈 LLM 리더보드의 백엔드로 사용되며, 재현 가능한 평가를 위해 공개 프롬프트를 기반으로 합니다. CLI 및 YAML 구성 파일을 통해 모델 평가, 멀티GPU 지원, 로깅 및 시각화 기능을 제공합니다.  

**핵심 기능**:  
- 60개 이상의 학술 벤치마크 통합  
- HuggingFace, vLLM, API 기반 모델 평가 지원  
- 멀티GPU 및 메모리 최적화 추론  
- 프롬프트 설계(Jinja2), 구성 기반 작업 설정  
- Weights & Biases 및 Zeno를 통한 결과 시각화  
- 다양한 양자화 및 분산 추론 기술 지원  

**주요 사용 사례**:  
- LLM 성능 벤치마킹  
- 프롬프트 엔지니어링 실험  
- 모델 백엔드 간 비교 평가  
- 연구 및 논문용 재현 가능한 실험 설계