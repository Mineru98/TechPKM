---
Language: Python
tags:
 - 한국어-NLP
 - 문장-임베딩
 - sentence-transformers
 - 파인튜닝
 - KoBERT
aliases:
 - ko-sentence-transformers
 - 한국어-문장-임베딩
 - ko-sbert
 - ko-roberta
url: https://github.com/jhgan00/ko-sentence-transformers
---
이 프로젝트는 한국어 사전학습 모델을 기반으로 한국어 문장 임베딩 모델을 제공합니다. 카카오브레인의 KorNLU 데이터셋(KorNLI, KorSTS)으로 파인튜닝된 모델을 `sentence-transformers` 라이브러리에서 쉽게 사용할 수 있도록 구현했으며, 멀티태스크 학습 모델을 포함해 다양한 한국어 문장 유사도 평가가 가능합니다. 허깅페이스 모델 허브에 공개된 사전 학습 모델은 문장 간 유사도 검색 등 NLP 작업에 최적화되어 있습니다.