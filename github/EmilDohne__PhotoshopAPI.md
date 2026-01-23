---
Language: C++20
tags:
 - Photoshop 파일 편집
 - C++ 라이브러리
 - Python 바인딩
 - 이미지 처리
 - 레이어 편집
aliases:
 - PhotoshopAPI
 - 포토샵 파일 포맷 파서
 - PSD 편집 라이브러리
url: https://github.com/EmilDohne/PhotoshopAPI
---
PhotoshopAPI는 Photoshop 파일(*.psd, *.psb)을 읽고 쓰기 위한 C++20 기반 라이브러리로, Python 바인딩을 제공합니다. 기존 라이브러리들과 달리 8/16/32비트 심도 지원과 레이어 편집을 중점으로 설계되었으며, Photoshop 대비 5~10배 빠른 읽기 속도와 20배 빠른 쓰기 성능을 자랑합니다. 스마트 오브젝트, 픽셀 마스크, 블렌드 모드 등 핵심 기능을 지원하며, 향후 조정 레이어 및 벡터 마스크 지원을 계획 중입니다. Photoshop 라이선스 없이 파일 조작이 가능해 자동화된 이미지 처리 파이프라인에 최적화되었습니다.