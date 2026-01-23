---
Language: Python
tags:
 - 한국어 임베딩
 - 문장 유사도
 - sentence-transformers
 - 파인튜닝
 - NLI/STS
aliases:
 - ko-sentence-transformers
 - 한국어 문장 임베딩
 - ko-sroberta-multitask
 - ko-sbert-multitask
url: https://github.com/jhgan00/ko-sentence-transformers
---
이 프로젝트는 한국어 문장 임베딩을 위해 KLUE 기반 모델을 KorNLI/KorSTS 데이터셋으로 파인튜닝한 한국어 sentence-transformers 구현체입니다. 카카오브레인의 KorNLU 데이터셋을 활용하여 NLI(자연어 추론) 및 STS(문장 유사도) 태스크에 최적화된 모델을 개발하였으며, 허깅페이스 허브에 공개된 모델은 `sentence-transformers` 라이브러리와 호환되어 한국어 문장 간 유사도 분석이 가능합니다. 멀티태스크 학습 모델(ko-sroberta-multitask)이 84.77의 최고 성능을 기록하며, ONNX 변환 및 자바 예시도 지원합니다.