---
Language: Python
tags:
 - NLP
 - 한국어-임베딩
 - DeBERTa
 - 금융-도메인
 - 유사도-계산
aliases:
 - kf-deberta-multitask
 - 금융-문장-임베딩
 - 한국어-문장-유사도
url: https://github.com/upskyy/kf-deberta-multitask
---
카카오뱅크의 kf-deberta-base 모델을 KorNLI/KorSTS 데이터셋으로 파인튜닝한 한국어 문장 임베딩 모델입니다. 금융 도메인 문장 간 유사도 계산 및 검색에 특화되어 있으며, 다양한 거리 메트릭에서 최고 수준의 성능(코스인 피어슨 85.75)을 보입니다. sentence-transformers 라이브러리와 호환되며, ONNX 변환 및 벤치마크 평가 기능이 제공됩니다.