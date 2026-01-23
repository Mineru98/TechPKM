---
Language: Python
tags:
 - 문서 레이아웃 분석
 - YOLO-v10
 - 합성 데이터
 - 실시간 모델
 - 딥러닝
aliases:
 - DocLayout-YOLO
 - 문서 레이아웃 감지
 - 글로벌-로컬 적응 인식
url: https://github.com/opendatalab/DocLayout-YOLO
---
DocLayout-YOLO는 YOLO-v10 기반의 실시간 문서 레이아웃 감지 모델로, 다양한 문서 유형에 대해 정확하고 빠른 객체 감지를 제공합니다. DocSynth-300K라는 대규모 합성 데이터셋을 활용한 사전 학습과, 글로벌-로컬 적응 인식 모듈을 통해 다양한 크기의 문서 요소를 정밀하게 감지하도록 설계되었습니다. 이 프로젝트는 PyTorch로 구현되었으며, Hugging Face를 통해 온라인 데모, 사전 학습된 모델, 데이터셋 등을 제공합니다. 주요 기능으로는 PDF 문서 콘텐츠 추출, 배치 추론 지원, Hugging Face 사전 학습 모델 로딩 등이 포함됩니다.