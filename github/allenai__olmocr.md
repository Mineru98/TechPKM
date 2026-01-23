---
Language: Python  
tags:  
 - OCR  
 - Vision Language Model  
 - PDF 처리  
 - 문서 변환  
 - GPU 가속  
aliases:  
 - olmOCR  
 - AllenAI OCR  
 - PDF 텍스트 추출  
 - 문서 OCR 도구  
url: https://github.com/allenai/olmocr  
---  
olmOCR은 PDF, PNG, JPEG 기반 문서를 깨끗한 Markdown 형식의 텍스트로 변환하는 도구입니다. 방정식, 표, 필기체, 복잡한 서식을 지원하며 헤더/푸터 자동 제거 및 자연스러운 읽기 순서 보장이 특징입니다. 7B 파라미터 VLM(Vision Language Model) 기반으로 GPU가 필요하며, 효율적인 처리(백만 페이지 당 약 $200)로 대규모 문서 변환에 적합합니다.  

주요 기능:  
- 다중 열, 이미지, 삽입 요소가 있는 문서의 구조적 텍스트 추출  
- 벤치마크 기반 성능 검증(olmOCR-Bench)  
- Docker 지원 및 분산 처리 기능(S3/Beaker 연동)  
- 외부 추론 서버(vLLM, Cirrascale 등)와의 호환성  

이 도구는 학술 논문, 보고서, 스캔 문서 등 다양한 이미지 기반 문서를 디지털 텍스트 형식으로 변환하는 데 최적화되어 있습니다.