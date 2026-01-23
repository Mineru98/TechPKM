---
Language: Python  
tags:  
 - OCR  
 - 문서 레이아웃 파싱  
 - 비전-언어 모델  
 - 다국어 지원  
 - 딥러닝  
aliases:  
 - dots.ocr  
 - 다국어 문서 파서  
 - 단일 VLM 기반 OCR  
url: https://github.com/rednote-hilab/dots.ocr/blob/master/README.md  
---
**dots.ocr**은 단일 비전-언어 모델(VLM)을 기반으로 텍스트 인식, 표/수식 감지, 읽기 순서 유지 등의 기능을 통합한 다국어 문서 파서입니다. 1.7B 파라미터의 경량화된 LLM을 기반으로 SOTA 수준의 성능을 달성하며, 복잡한 멀티모델 파이프라인 대신 프롬프트 변경만으로 다양한 작업을 처리할 수 있는 간결한 아키텍처가 특징입니다. 영어, 중국어, 저자원 언어 등 다양한 언어에서 뛰어난 성능을 보이며, HuggingFace, vLLM 등을 통해 쉽게 배포할 수 있습니다.  

> 주요 기능:  
> - 단일 VLM으로 레이아웃 감지 + 콘텐츠 인식 통합  
> - 다국어 문서 지원 및 OmniDocBench 등 벤치마크에서 SOTA 성능  
> - 텍스트, 표, 수식, 읽기 순서 동시 처리  
> - Docker 및 vLLM을 통한 효율적 배포 지원