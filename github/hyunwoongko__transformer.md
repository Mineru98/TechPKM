---
Language: Python
tags:
 - Transformer
 - NLP
 - 딥러닝
 - 기계번역
 - PyTorch
aliases:
 - Transformer-구현
 - Ko-Hyunwoong-Transformer
 - Multi30K-번역모델
url: https://github.com/hyunwoongko/transformer
---
이 프로젝트는 2017년 "Attention is All You Need" 논문에 기반한 Transformer 모델을 직접 구현한 코드입니다. Positional Encoding, Multi-Head Attention, Feed Forward Network 등 핵심 구성요소를 포함하며, Multi30K 데이터셋으로 독일어-영어 번역 실험을 수행했습니다. 원본 논문과 유사한 하이퍼파라미터(8개 헤드, 6개 레이어, 512차원)를 사용했으나, 저자는 코드 완성도와 정확성을 보장하지 않는다고 경고합니다. BLEU 점수 26.4로 WMT14 기준(25.8)보다 약간 높은 성능을 기록했습니다.