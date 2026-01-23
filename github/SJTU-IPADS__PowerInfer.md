---
Language: C++/Python  
tags:  
 - LLM 추론 엔진  
 - GPU/CPU 하이브리드  
 - 고속 추론  
 - 로컬 배치  
 - 스파스 모델  
aliases:  
 - PowerInfer  
 - 파워인퍼  
 - SJTU-IPADS PowerInfer  
url: https://github.com/SJTU-IPADS/PowerInfer  
---  
PowerInfer는 소비자용 GPU에서 동작하는 고속 대규모 언어 모델(LLM) 추론 엔진입니다. 활성화 국지성(activation locality)과 '핫/콜드 뉴런' 개념을 활용하여 GPU 메모리 사용량을 줄이고 CPU-GPU 간 데이터 전송을 최적화합니다. RTX 4090에서 최대 29.08토큰/초의 성능을 달성하며, llama.cpp 대비 최대 11.69배 빠른 속도로 작동합니다. ReLU 스파스 모델과 호환되며 로컬 배치에 특화되어 있습니다.  

핵심 기술:  
- **활성화 국지성 기반 설계**: 핫 뉴런(빈번히 활성화)을 GPU에 미리 로드하고 콜드 뉴런(입력 의존적)은 CPU에서 처리하여 효율성 향상  
- **하이브리드 CPU/GPU 활용**: 리소스 요구사항 감소 및 처리 속도 개선  
- **적응형 예측기 통합**: 뉴런 활성화 및 계산 스파스성 최적화  

지원 모델: Falcon-40B, Llama2 계열, ProSparse Llama2, Bamboo-7B 등. Linux/Windows/ARM 기반 애플 M 시리즈에서 동작하며 AMD ROCm 및 향후 Metal 백엔드 지원 예정.