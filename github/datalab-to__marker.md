---
Language: Python  
tags:  
 - 문서 변환  
 - OCR  
 - PDF 처리  
 - 마크다운 생성  
 - 딥러닝  
aliases:  
 - 마커  
 - Marker  
 - 문서 파서  
 - PDF to Markdown  
url: https://github.com/datalab-to/marker  
---
Marker는 다양한 형식의 문서를 정확하고 빠르게 마크다운, JSON, HTML 등으로 변환하는 오픈소스 도구입니다. PDF, 이미지, PPTX, DOCX 등의 문서를 처리하며 표, 수식, 코드 블록, 이미지 추출 등 풍부한 기능을 제공합니다. OCR 기술을 활용해 디지털화되지 않은 문서도 분석 가능하며, LLM(Large Language Model)을 통한 정확도 향상 모드를 지원합니다. GPU/CPU/MPS 환경에서 작동하며, 확장 가능한 아키텍처로 사용자 정의 포맷팅이 가능합니다. 연구, 개인 사용, 스타트업에 무료로 제공되며, 상용 라이선스는 별도 제공됩니다.  

### 핵심 기능  
- **다양한 포맷 지원**: PDF, 이미지, PPTX, DOCX, XLSX, HTML, EPUB  
- **구조화된 데이터 추출**: 표, 수식, 코드 블록, 이미지  
- **고정밀 OCR**: LaTeX 수식 변환 및 레이아웃 감지  
- **LLM 통합**: 테이블 병합, 인라인 수학 처리 등 정확도 향상  
- **확장성**: 사용자 정의 프로세서 및 렌더러 추가 가능  

### 사용 사례  
- 학술 논문, 교재, 재무제표 등의 구조화  
- RAG(Retrieval-Augmented Generation)를 위한 청크 생성  
- 문서 디지털화 및 검색 가능한 아카이브 구축  

### 기술 스택  
- **백엔드**: Python, PyTorch  
- **OCR 엔진**: Surya  
- **LLM 서비스**: Gemini, Ollama, Claude, OpenAI, Azure OpenAI  

### 배포 옵션  
- 로컬 설치: `pip install marker-pdf`  
- 온프레미스 솔루션: 상용 라이선스  
- 클라우드 API: [Datalab.to 플랫폼](https://datalab.to)  

### 주요 성능  
- 단일 H100 GPU 기준 25페이지/초 처리 속도  
- 벤치마크에서 Llamaparse, Mathpix 대비 높은 정확도 달성  

이 프로젝트는 문서 인텔리전스 분야에서 오픈소스 대안으로 주목받으며, 연구 및 상업적 활용을 위해 지속적으로 개선되고 있습니다.