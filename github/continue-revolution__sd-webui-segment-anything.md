---
Language: Python  
tags:  
 - Stable Diffusion  
 - 이미지 분할  
 - AI 확장  
 - ControlNet 통합  
 - 세그멘테이션  
aliases:  
 - sd-webui-segment-anything  
 - SAM 확장  
 - GroundingDINO 통합  
url: https://github.com/continue-revolution/sd-webui-segment-anything  
---  
이 프로젝트는 Stable Diffusion WebUI와 ControlNet 확장에 Segment Anything(SAM) 및 GroundingDINO 기술을 통합하여 이미지 편집 기능을 향상시키는 것을 목표로 합니다. 클릭 기반 세그멘테이션 마스크 생성, 텍스트 프롬프트를 활용한 경계 상자 추출, 컨트롤넷 인페인팅 지원, 자동 이미지 매팅 및 LoRA/LyCORIS 훈련 세트 생성 등의 기능을 제공합니다. 다양한 세그멘테이션 모델(SAM, SAM-HQ, MobileSAM)과 호환되며, API를 통해 단일 이미지 처리 기능을 지원합니다.  

핵심 기능으로는 마스크 확장, GroundingDINO 통합, ControlNet V1.1 인페인팅 지원, EditAnything 및 AutoSAM 통합이 포함되며, 배치 처리 및 카테고리 기반 마스크 생성 기능도 제공합니다. CPU 지원 및 로컬 GroundingDINO 옵션을 통해 호환성과 접근성을 개선했습니다.