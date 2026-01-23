---
Language: C++  
tags:  
 - 서브워드 토크나이저  
 - 자연어 처리  
 - 머신러닝  
aliases:  
 - SentencePiece  
 - 서브워드 분할  
 - BPE 토크나이저  
url: https://github.com/google/sentencepiece  
---
SentencePiece는 신경망 기반 텍스트 생성 시스템을 위한 비지도 학습 텍스트 토크나이저 및 디토크나이저입니다. 고정 크기의 어휘 집합이 미리 결정된 환경에서 바이트-페어 인코딩(BPE) 및 유니그램 언어 모델을 지원하며, 언어 독립적인 처리가 가능합니다. 주요 특징은 사전 토크나이징 불필요, 서브워드 정규화, 빠른 처리 속도 등입니다. Python 및 C++ 라이브러리를 제공하며, NMT(신경망 기계 번역) 모델의 강건성과 정확도 향상에 기여합니다.  

- **핵심 기술**: 서브워드 분할 알고리즘(BPE/유니그램), 언어 독립 처리, 서브워드 정규화 지원  
- **사용 사례**: 영어/중일어 등 언어별 토크나이징, 신경망 번역 시스템의 전처리  
- **특징**: 고정 어휘 크기, NFKC 정규화, 메타 기호(▁)를 통한 공백 보존  
- **설치**: `pip install sentencepiece` 또는 C++ 소스 빌드  
- **활용**: `spm_train`으로 모델 학습 후 `spm_encode`/`spm_decode`로 텍스트 처리  

> 기술적 세부 사항은 [공식 문서](https://github.com/google/sentencepiece) 참조.