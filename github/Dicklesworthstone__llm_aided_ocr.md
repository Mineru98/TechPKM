---
Language: Python
tags:
 - OCR
 - 자연어처리
 - LLM
 - 문서변환
 - Tesseract
aliases:
 - LLM-Aided OCR
 - OCR 오류 수정
 - PDF 텍스트 추출
 - LLM 문서 정제
url: https://github.com/Dicklesworthstone/llm_aided_ocr
---
이 프로젝트는 OCR 출력 품질을 향상시키기 위한 시스템으로, PDF 문서를 이미지로 변환한 후 Tesseract OCR로 텍스트를 추출하고, LLM(대형 언어 모델)을 활용해 오류 수정 및 마크다운 포맷팅을 수행합니다. 로컬 또는 클라우드 기반 LLM(OpenAI, Anthropic)을 지원하며, 텍스트 청킹, 토큰 관리, 품질 평가 기능을 포함해 다양한 문서 처리 요구사항을 충족합니다. 비동기 처리와 GPU 가속을 통해 성능을 최적화하였습니다.