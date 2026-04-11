---
Language: Python
tags:
 - 자연어처리
 - 형태소분석
 - 한국어
 - Mecab
 - NLP
aliases:
 - Pecab
 - Pure Python Mecab
 - 피캡
url: https://github.com/hyunwoongko/pecab/blob/main/README.md
---
기존 Mecab의 뛰어난 성능을 계승하면서도 복잡한 설치 과정 없이 pip으로 쉽게 설치할 수 있는 순수 파이썬 기반 한국어 형태소 분석기입니다. 제로 카피 메모리 매핑과 더블 어레이 트라이(DATrie)를 적용하여 기존 라이브러리 대비 로딩 속도를 50~100배 이상 향상시키고 메모리 사용량을 대폭 줄였습니다. KoNLPy와 유사한 직관적이고 파이썬다운 API를 제공하여 사용자 사전 추가 및 복합명사 분해 등의 기능을 손쉽게 사용할 수 있습니다.