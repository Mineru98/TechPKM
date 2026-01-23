---
Language: Python  
tags:  
 - OCR  
 - macOS  
 - VisionFramework  
 - 이미지처리  
 - 텍스트인식  
aliases:  
 - ocrmac  
 - MacOCR  
 - AppleVisionOCR  
 - 라이브텍스트OCR  
url: https://github.com/straussmaximilian/ocrmac  
---  
ocrmac은 macOS 시스템(10.15 이상)에서 이미지의 텍스트를 추출하는 Python 래퍼 프로젝트입니다. Apple의 Vision Framework 또는 LiveText 기능을 활용하여 이미지 내 텍스트, 신뢰도, 경계 상자를 반환하며, PIL 이미지 객체나 경로 입력을 지원합니다. 빠른 처리(`fast`) 또는 정확한 인식(`accurate`) 모드 선택은 물론, 언어 선호도 설정과 시각화된 주석 추가 기능도 제공합니다. Mac 사용자 대상 CPU 기반 OCR 솔루션으로 Tesseract나 EasyOCR의 대체제로 개발되었습니다.