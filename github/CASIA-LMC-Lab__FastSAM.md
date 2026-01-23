---
Language: Python  
tags:  
 - 객체 분할  
 - 실시간 처리  
 - 세그멘테이션  
 - 컴퓨터 비전  
 - AI 모델  
aliases:  
 - FastSAM  
 - Fast Segment Anything Model  
 - CNN 세그멘테이션  
 - 실시간 SAM 모델  
url: https://github.com/CASIA-IVA-Lab/FastSAM  
---
FastSAM은 SA-1B 데이터셋의 2%만 사용하여 훈련된 CNN 기반 세그멘테이션 모델로, SAM(기존 Segment Anything Model)과 유사한 성능을 유지하면서 50배 빠른 처리 속도를 제공합니다. 텍스트, 박스, 포인트 프롬프트와 "모든 것(everything)" 모드를 지원하며, 다양한 다운스트림 작업(예: 이상 감지, 건물 추출)에 적용 가능합니다. YOLOv8x 기반으로 구현되어 효율적인 실시간 분할이 특징입니다.