---
Language: C++
tags:
 - 서브워드 토크나이저
 - 자연어 처리
 - 머신러닝
aliases:
 - SentencePiece
 - 서브워드 분할기
 - NMT 토크나이저
url: https://github.com/google/sentencepiece
---
SentencePiece는 신경망 기반 텍스트 생성 시스템을 위한 비지도 학습 기반 텍스트 토크나이저 및 디토크나이저입니다. 미리 정의된 어휘 크기를 기반으로 BPE(Byte-Pair-Encoding) 및 유니그램 언어 모델 알고리즘을 지원하며, 언어 독립적인 처리가 가능합니다. 공백 처리, 서브워드 정규화, 빠른 처리 속도 등의 특징을 갖추고 있어 일본어/중국어 같은 공백 없는 언어 처리에 적합합니다. 주요 기술로는 데이터 기반 토크나이징, NFKC 정규화, 직접 어휘 ID 생성이 포함됩니다.