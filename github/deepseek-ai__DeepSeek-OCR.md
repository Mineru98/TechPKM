---
Language: Python
tags:
 - OCR
 - 딥러닝
 - 문서처리
 - 멀티모달
 - 허깅페이스
aliases:
 - DeepSeek-OCR
 - DeepSeek OCR
 - 문서 이미지 압축
 - 멀티모달 OCR 모델
 - DeepSeek-OCR-메타데이터
url: https://github.com/deepseek-ai/DeepSeek-OCR
---
DeepSeek-OCR은 LLM 중심 관점에서 비전 인코더의 역할을 연구하기 위한 OCR 모델입니다. 이미지 및 PDF 문서에서 텍스트 추출, 마크다운 변환, 레이아웃 분석 등 다양한 문서 처리 기능을 제공하며, vLLM 및 Hugging Face Transformers를 통해 추론이 가능합니다. Tiny에서 Large까지 다양한 해상도 모드와 동적 해상도 지원을 통해 유연한 문서 분석이 가능합니다.  

**핵심 기능**:  
- 이미지/PDF → 텍스트/마크다운 변환  
- 레이아웃 인식 OCR 및 일반 이미지 설명 생성  
- vLLM 및 Transformers 기반 추론 지원  
- 다양한 해상도 모드(Tiny/Small/Base/Large) 및 동적 해상도(Gundam) 지원  

**특징**:  
- Flash Attention 2 기반의 효율적인 추론  
- Hugging Face 및 공식 GitHub에서 모델 가중치 제공  
- 논문(arXiv:2510.18234)과 벤치마크 지원  

**사용 사례**:  
- 문서 디지털화, 자동화된 데이터 추출, 학술 논문 분석, 멀티모달 LLM 통합 등.