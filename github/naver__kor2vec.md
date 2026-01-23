---
Language: Python
tags:
 - 한국어 임베딩
 - Word2Vec 대체
 - Char-word Encoder
 - NLP
 - OOV 해결
aliases:
 - kor2vec
 - 한국어 임베딩 솔루션
 - 교착어 임베딩
 - Yoon Kim 모델 적용
url: https://github.com/naver/kor2vec
---
kor2vec은 한국어 교착어 특성을 고려한 CNN 기반 Char-word 임베딩 솔루션입니다. 기존 토크나이저 의존적 임베딩 방식의 OOV 문제와 병목 현상을 해결하기 위해 Yoon Kim의 문자 인식 언어 모델을 적용했습니다. 한국어 문장을 형태소 분석 없이 직접 임베딩 벡터로 변환할 수 있으며, PyTorch 통합이 용이합니다. "안녕 아이오아이야" 같은 복합 형태도 정확히 처리하는 것이 핵심 특징입니다.