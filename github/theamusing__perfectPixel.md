---
Language: Python
tags:
 - PixelArt
 - ImageProcessing
 - OpenCV
 - AI-Image
 - ComfyUI
aliases:
 - Perfect Pixel
 - 퍼펙트 픽셀
 - 픽셀 아트 보정 도구
url: https://github.com/theamusing/perfectPixel/blob/main/readme.md
---
AI로 생성된 픽셀 아트 이미지에서 격자 크기를 자동으로 감지하고, 왜곡된 픽셀을 완벽하게 정렬된 형태로 보정해 주는 파이썬 라이브러리입니다. 기존 스케일링 방식의 한계를 극복하기 위해 FFT 및 소벨 엣지 검출 알고리즘을 활용하여 최적의 그리드를 추출합니다. 오픈CV 기반과 NumPy만 사용하는 경량 버전을 모두 지원하며, ComfyUI 노드로도 연동할 수 있어 다양한 이미지 생성 워크플로우에 쉽게 통합할 수 있습니다.