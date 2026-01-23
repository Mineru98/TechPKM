---
Language: Python
tags:
 - OCR
 - Tesseract
 - Docker
 - Flask
 - 이미지처리
aliases:
 - OCR Tesseract Docker
 - Tesseract OCR Docker
 - 이미지 텍스트 추출
 - Docker 기반 OCR
url: https://github.com/ricktorzynski/ocr-tesseract-docker
---
이 프로젝트는 Tesseract OCR 기술을 활용해 이미지 내 텍스트를 추출하는 Flask 기반 웹 애플리케이션입니다. Docker로 패키징되어 로컬 환경에서 쉽게 실행 가능하며, OpenCV를 사용해 이미지 노이즈를 줄여 OCR 정확도를 향상시켰습니다. AWS Elastic Beanstalk에 배포 가능한 구조로 설계되었으나 현재는 로컬 개발/테스트용으로 권장됩니다. Python 3.6으로 업데이트되어 최신 환경에서도 호환됩니다.