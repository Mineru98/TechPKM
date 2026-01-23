---
Language: Python  
tags:
 - OCR 처리
 - Streamlit 앱
 - 로컬 AI 모델
 - PDF 분석
 - CLI 도구  
aliases:
 - LocalOCR
 - Curiosity AI Scans
 - Ollama 통합 OCR
 - 로컬 비전 모델  
url: https://github.com/Curiosity-Ai-BV/localOCR  
---
이 프로젝트는 로컬 AI 비전 모델(Ollama 기반)과 Streamlit 인터페이스를 결합하여 이미지 및 PDF 문서를 분석하는 애플리케이션입니다. 사용자는 여러 파일을 업로드한 후 Gemma 3, Llama 3.2 Vision 등의 모델로 상세 설명을 생성하거나 특정 필드(청구 번호, 날짜 등)를 추출할 수 있으며, PDF를 페이지 단위로 처리하거나 전체 문서로 처리할 수 있습니다. CLI를 통해 헤드리스 배치 작업도 지원하며, 결과를 CSV 형식으로 내보낼 수 있습니다. 성능 최적화를 위한 다양한 설정(이미지 크기, JPEG 품질, PDF 렌더링 스케일)과 추출 모드용 JSON 스키마/템플릿 시스템을 제공합니다.  

주요 기술 스택은 Python, Streamlit, PyMuPDF, Pillow이며, Ollama를 통해 로컬에서 모델을 실행합니다. 모듈화된 구조(core, adapters, ui, utils)로 유지보수와 확장성이 뛰어납니다.