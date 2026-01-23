---
Language: Python  
tags:  
 - LLM 추론 최적화  
 - 메모리 효율화  
 - 경량화 기술  
 - 오픈소스 모델 지원  
 - GPU 리소스 절약  
aliases:  
 - AirLLM  
 - 경량 LLM 추론  
 - 4GB GPU LLM  
url: https://github.com/lyogavin/airllm  
---
AirLLM은 대용량 언어 모델(LLM)의 추론 메모리 사용을 최적화하여 4GB GPU에서 70B 모델, 8GB GPU에서 405B Llama3.1 모델을 양자화/가지치기 없이도 실행할 수 있도록 지원합니다. 주요 기능으로는 블록 단위 양자화 기반 압축(최대 3배 속도 향상), 다양한 오픈소스 모델(ChatGLM, QWen, Baichuan, Mistral 등) 지원, MacOS 호환성, Hugging Face 통합 등을 제공합니다.  

### 핵심 특징  
- 70B 이상 모델을 4GB GPU에서 실행 가능  
- 3x 추론 속도 향상(블록 단위 양자화)  
- ChatGLM/QWen/Baichuan/Mistral 등 10+ 모델 지원  
- Hugging Face 허브 및 로컬 모델 호환  
- macOS 및 CPU 추론 지원  
- 자동 모델 타입 감지(AutoModel)  

### 기술 스택  
- Python, Hugging Face, bitsandbytes(양자화), PyTorch  
- Safari Tensors 지원(모든 상위 10개 LLM 리더보드 모델 호환)  

### 활용 시나리오  
- 제한된 GPU 자원에서 대용량 모델 추론 필요 시  
- 실시간 응답이 필요한 경량화된 LLM 서비스 구축  
- 연구/교육용 고성능 모델 테스트 환경 구성  

> 📌 "70B 모델을 4GB GPU에서 실행한다"는 점이 가장 혁신적인 특징입니다. 기존 양자화 기술과 달리 가중치만 압축하여 정확도 손실 최소화.