---
Language: Python  
tags:  
 - Streamlit  
 - Ollama  
 - AI 비전 모델  
 - 이미지 분석  
 - PDF 처리  
aliases:  
 - Curiosity AI Scans  
 - 로컬 AI 모델 분석기  
 - 이미지 PDF AI 추출  
url: https://github.com/ad1x/curiosity-ai-scans  
---  
이 프로젝트는 로컬 AI 비전 모델(Gemma 3, Llama 3.2 Vision 등)과 Ollama를 연동한 Streamlit 기반 이미지/PDF 분석 앱입니다. 다중 파일 업로드, 모델 선택, 상세 설명 생성 또는 구조화된 필드 추출(청구서 번호, 날짜 등) 기능을 제공하며, 결과를 CSV로 내보낼 수 있습니다. PDF는 페이지별 또는 전체 문서 단위로 처리 가능하며, 고급 모델 설정(온도, 토큰 제한, 시스템 프롬프트)과 UI 커스터마이징(컴팩트 모드)을 지원합니다. CLI를 통한 헤드리스 배치 처리도 가능합니다.