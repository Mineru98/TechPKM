---
Language: Python  
tags:  
 - OCR  
 - macOS  
 - 이미지처리  
 - VisionFramework  
 - PyObjC  
aliases:  
 - ocrmac  
 - macOCR  
 - 파이썬OCR  
 - 이미지텍스트추출  
url: https://github.com/straussmaximilian/ocrmac  
---  
Mac 시스템에서 이미지를 통해 텍스트를 추출하는 Python 래퍼 프로젝트. Apple의 Vision Framework 또는 LiveText 기능을 활용하여 이미지 내 텍스트, 신뢰도, 경계 상자 정보를 반환. macOS 10.15 이상에서 동작하며, PIL 이미지 객체 또는 이미지 경로를 직접 전달 가능. 빠른 처리 속도와 높은 정확도를 지원하는 것이 핵심 특징이며, 다양한 언어 필터링을 통해 텍스트 인식 결과를 개선할 수 있음.  

> 📌 **핵심 기능**:  
> - `fast`/`accurate` 인식 수준 선택  
> - 언어 선호도 설정 (`['en-US', 'zh-Hans']` 등)  
> - LiveText 지원 (macOS Sonoma 이상)  
> - 경계 상자 시각화 (PIL/매트플롯립)  
> - 클래스/함수 형태 모두 사용 가능 (`ocrmac.OCR` 또는 `ocrmac.text_from_image`)