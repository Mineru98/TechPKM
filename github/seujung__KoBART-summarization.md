---
Language: Python
tags:
 - summarization
 - BART
 - Korean NLP
 - KoBART
 - text-generation
aliases:
 - KoBART-summarization
 - 한국어 요약 모델
 - kobart-base-v1
 - 문서 요약
url: https://github.com/digit82/KoBART-summarization
---
이 프로젝트는 한국어 문서 요약 생성을 위한 KoBART 모델을 구현한 리포지토리입니다. Dacon 경진대회 데이터를 학습한 요약 모델을 제공하며, 34k+ 학습 데이터와 8.5k 테스트 데이터를 활용해 fine-tuning되었습니다. ROUGE-1 F1 0.505, ROUGE-2 F1 0.340의 성능을 보이며, Streamlit 기반 데모 페이지와 모델 추론 파이프라인을 포함합니다. HuggingFace 호환 포맷의 모델 바이너리를 제공합니다.