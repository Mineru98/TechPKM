---
Language: Python  
tags:  
 - 금융 LLM  
 - 오픈소스 모델  
 - LoRA  
 - 주식 예측  
 - 감정 분석  
aliases:  
 - FinGPT  
 - 금융 GPT  
 - 오픈소스 금융 LLM  
url: https://github.com/AI4Finance-Foundation/FinGPT  
---
FinGPT는 금융 분야에 특화된 오픈소스 대형 언어 모델(LLM)로, 실시간 데이터 업데이트와 경량화를 통해 BloombergGPT 등의 상용 모델에 대한 대안을 제공합니다. LoRA 기반 파인튜닝으로 저비용·고효율 학습이 가능하며, 감정 분석·주가 예측·문서 요약 등 20가지 이상의 금융 애플리케이션을 지원합니다. 다중 작업(멀티태스크) 및 단일 작업 모델, RAG(검색 증강 생성) 프레임워크 등 다양한 금융 NLP 기능을 포함합니다. Hugging Face에서 모델·데이터셋·데모를 제공하며, RTX 3090 단일 GPU로도 훈련이 가능합니다.  

### 핵심 특징  
- **저비용 학습**: LoRA 기법으로 RTX 3090에서 8비트 양자화 시 6.47달러 비용으로 파인튜닝  
- **다양한 태스크**: 감정 분석·관계 추출·헤드라진 분류·개체명 인식 등  
- **실시간 적응**: 월별/주별 업데이트를 위한 데이터 파이프라인 구축  
- **오픈소스 생태계**: FinNLP·FinGPT-Benchmark·FinGPT-RAG 등 하위 프로젝트 연계  

### 주요 성능  
- **감정 분석 가중치 F1 점수**: 0.882 (FinGPT v3.3 기준)  
- **BloombergGPT 대비 1/10,000 비용**: 53일·267만 달러 대비 17.25시간·17.25달러  

### 활용 분야  
- 로보 어드바이저, 금융 리포트 요약, 실시간 시장 분석, 멀티모달 데이터 처리 등  

### 논문 및 데모  
- IJCAI·NeurIPS 워크숍 논문 5편 게재, Hugging Face에서 실시간 예측 데모 제공  
- [FinGPT-Forecaster](https://huggingface.co/spaces/FinGPT/FinGPT-Forecaster) 데모: 티커 심볼 입력 시 주가 변동 예측  

### 기술 스택  
- Python 기반, Hugging Face·PyTorch 연동, LoRA·QLoRA 학습 지원  
- Llama2·Falcon·ChatGLM2 등 오픈소스 베이스 모델 통합  

### 라이선스  
MIT License (학술·연구 목적 사용 권장)  

> **경고**: 본 프로젝트는 학술 연구용이며, 실제 투자 자문으로 사용될 수 없습니다. 거래 전 전문가 상담이 필수입니다.