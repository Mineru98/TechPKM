---
Language: Python  
tags:  
 - 컴퓨터비전  
 - 객체 검출  
 - 세그멘테이션  
 - 비디오 트래킹  
 - 오픈소스 모델  
aliases:  
 - Grounded SAM 2  
 - 객체 검출 및 트래킹  
 - SAM 2  
 - Grounding DINO  
url: https://github.com/IDEA-Research/Grounded-SAM-2  
---  
Grounded SAM 2는 비디오 내에서 텍스트 기반으로 객체를 검출, 세그멘테이션 및 트래킹할 수 있는 통합 파이프라인 프로젝트입니다. Grounding DINO, DINO-X, SAM 2 등의 모델을 결합하여 이미지/비디오에서 객체 인식 및 추적 작업을 수행하며, API 및 로컬 환경에서의 유연한 실행이 가능합니다. 고해상도 이미지 처리 및 SAHI(타일 기반 추론)를 지원하며, 다양한 프롬프트 유형(박스, 마스크, 포인트)을 활용한 트래킹 기능을 제공합니다.  

> 📌 핵심 기능:  
> - **Grounding + Segmentation**: 텍스트 프롬프트 기반 객체 검출 및 분할  
> - **비디오 트래킹**: 객체 ID 연속성 유지 및 실시간 카메라 스트림 처리  
> - **고해상도 처리**: SAHI를 통한 4K 이미지 분석 지원  
> - **다중 모델 통합**: Grounding DINO 1.5/1.6, DINO-X, SAM 2, Florence-2와의 호환성  
> - **자동 라벨링**: 이미지 캡션 → 객체 검출 → 세그멘테이션 파이프라인 제공