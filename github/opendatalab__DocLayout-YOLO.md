---
Language: Python
tags:
 - 문서 레이아웃 분석
 - YOLO-v10
 - 데이터 증강
 - 합성 데이터
 - 실시간 객체 감지
aliases:
 - DocLayout-YOLO
 - DocSynth-300K
 - 문서 구조 인식
url: https://github.com/opendatalab/DocLayout-YOLO
---
DocLayout-YOLO는 다양한 문서에 대한 실시간 및 정밀한 레이아웃 분석을 제공하는 모델입니다. YOLO-v10 기반으로 제작되었으며, 대규모 합성 문서 데이터셋인 DocSynth-300K를 활용한 사전 학습과 글로벌-로컬 적응 감지 모듈을 통한 구조적 최적화를 특징으로 합니다. 이 모델은 문서 내 다양한 크기와 형태의 요소(텍스트, 표, 이미지 등)를 정확하게 식별하는 데 특화되어 있으며, 온라인 데모와 사전 학습된 모델을 Hugging Face에서 제공합니다.  

주요 기능으로는 배치 추론 지원, PDF-Extract-Kit 통합, 다양한 공개 데이터셋(D4LA, DocLayNet) 평가 성능 향상 등이 있습니다.  
요약하면, DocLayout-YOLO는 합성 데이터 기반의 강력한 레이아웃 분석 솔루션으로, 연구 및 상업적 문서 처리 애플리케이션에 적합합니다.