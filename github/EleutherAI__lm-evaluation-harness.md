---
Language: Python  
tags:  
 - 언어 모델 평가  
 - 벤치마크 프레임워크  
 - LLM 평가  
aliases:  
 - LM Evaluation Harness  
 - 언어 모델 평가 도구  
 - 오픈 LLM 리더보드  
url: https://github.com/EleutherAI/lm-evaluation-harness  
---  
# 언어 모델 평가 하니스  

이 프로젝트는 다양한 생성형 언어 모델을 평가하기 위한 통합 프레임워크를 제공합니다. 60개 이상의 표준 학술 벤치마크와 수백 가지 하위 작업을 지원하며, 변환기(transformers), vLLM, API 기반 모델 등 다양한 백엔드를 통한 추론이 가능합니다. 허깅페이스 오픈 LLM 리더보드의 백엔드로 사용되며, NVIDIA, Cohere, BigScience 등 여러 조직에서 활용 중입니다.  

## 주요 기능  
- **다양한 백엔드 지원**: HuggingFace, vLLM, API 기반 모델(OpenAI, Anthropic), SGLang 등  
- **고급 구성 옵션**: 프롬프트 디자인, 출력 후처리, 다중 생성 설정, 피처 추출 지원  
- **멀티모달 평가**: 텍스트+이미지 입력 작업 및 프로토타이핑 기능  
- **성능 최적화**: 자동 배치 크기 조정, 병렬 처리, 메모리 효율성 개선  
- **확장성**: 사용자 정의 작업 및 모델 통합 용이  

이 도구는 모델 간 비교 가능성을 보장하며, 공개 프롬프트와 재현 가능한 평가 방식을 통해 연구 및 상용 환경에서 널리 활용됩니다.