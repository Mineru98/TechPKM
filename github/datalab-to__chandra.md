---
Language: Python  
tags:  
 - OCR  
 - 문서분석  
 - AI모델  
 - Python  
 - vLLM  
aliases:  
 - Chandra-OCR  
 - Datalab-OCR  
 - 문서지능모델  
 - 복합문서OCR  
url: https://github.com/datalab-to/chandra  
---  
Chandra는 복잡한 문서(필기, 표, 수학 방정식, 양식 등)를 처리하는 최첨단 OCR 모델입니다. 두 가지 추론 모드(HuggingFace/vLLM)와 레이아웃 인식 출력(Markdown, HTML, JSON)을 지원하며, 40개 이상의 언어를 처리합니다. 연구 및 상업적 활용을 위한 오픈소스 라이센스(Apache 2.0/수정 OpenRAIL-M)를 적용했습니다.  

**핵심 기능**:  
- 필기체, 표 구조(colspan/rowspan), 수학 방정식(LaTeX), 양식 필드 복원  
- Markdown/HTML/JSON 출력 및 바운딩 박스 좌표 포함  
- vLLM 서버 배포를 통한 생산성 최적화  
- CLI 및 Python API 지원