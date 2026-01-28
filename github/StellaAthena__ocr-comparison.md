---
Language: Python
tags:
 - OCR 비교
 - Tesseract
 - EasyOCR
 - 시각화
 - 정확도 평가
aliases:
 - OCR 엔진 비교 시스템
 - OCR 성능 평가 도구
 - OCR 비교 라이브러리
url: https://github.com/StellaAthena/ocr-comparison
---
이 프로젝트는 Tesseract와 EasyOCR 등의 OCR 엔진을 비교하고 정확도 지표(CER, WER)와 시각화를 제공하는 Python 라이브러리입니다. 확장 가능한 어댑터 아키텍처로 새로운 OCR 엔진 추가가 가능하며, CLI 및 Python API를 통해 단일 이미지 또는 배치 처리를 지원합니다. 주요 기능으로 여러 엔진 동시 비교, 텍스트 추출, 정확도 평가, 다양한 시각화 모드(분할 비교, 병렬 표시, 오버레이)를 제공합니다.