---
Language: Python  
tags:  
 - 이미지 분할  
 - 세그멘테이션 모델  
 - CLIP 통합  
 - 프롬프트 엔지니어링  
 - 컴퓨터 비전  
aliases:  
 - SAM-CLIP 통합  
 - 텍스트 프롬프트 세그멘테이션  
 - Segment Anything with CLIP  
url: https://github.com/Curt-Park/segment-anything-with-clip  
---  
이 프로젝트는 Meta의 Segment Anything Model(SAM)과 OpenAI의 CLIP을 결합하여 텍스트 프롬프트를 활용한 이미지 세그멘테이션을 구현한 것입니다. SAM으로 객체 제안을 생성한 후 CLIP을 통해 텍스트 쿼리와의 유사도를 계산해 특정 객체를 분할하는 방식을 제안합니다. 로컬 실행 및 Gradio 인터페이스를 지원하며, 컴퓨터 비전 분야의 프롬프트 기반 세그멘테이션 문제에 집중합니다. 주요 특징은 SAM의 객체 제안과 CLIP의 텍스트-이미지 유사도 계산을 결합한 혁신적인 접근법입니다.