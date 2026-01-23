---
Language: Python  
tags:  
 - Arxiv 번역  
 - 논문 요약  
 - 자연어 처리  
 - OCR 기술  
 - 웹 렌더링  
aliases:  
 - Arxiv 번역 프로젝트  
 - 논문 한글화  
 - Nougat OCR 활용  
url: https://github.com/kh-kim/arxiv-translator  
---  
이 프로젝트는 빠르게 증가하는 Arxiv 논문을 효율적으로 검토하기 위해 한글화된 웹페이지를 제공하는 것을 목표로 합니다. Nougat OCR 라이브러리를 활용해 다양한 형식의 PDF에서 텍스트를 추출하고, 자체 번역 모델을 통해 한국어 번역본을 생성합니다. 번역된 내용은 HTML로 변환되어 GitHub에 호스팅되며, Arxiv 원본 논문과 함께 제공됩니다. 이 프로젝트는 RAG(검색 증강 생성), 모델 병합, 소규모 언어 모델 최적화 등 최신 NLP 연구 동향을 다룹니다.  

> 🔍 핵심 특징:  
> - PDF→Markdown→HTML 변환 파이프라인  
> - 자체 개발 번역 모델(DeepL/Google 중간 수준 성능)  
> - 70+ 개의 최신 논문 한글화 샘플 포함  
> - 지속적인 확장 계획(이미지 처리 추가 등)