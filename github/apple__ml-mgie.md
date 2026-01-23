---
Language: Python
tags:
 - 멀티모달 AI
 - 이미지 편집
 - 딥러닝
 - MLLM
 - ICLR
aliases:
 - MGIE
 - MLLM-Guided Image Editing
 - 지시 기반 이미지 편집
 - multimodal image editing
url: https://github.com/timothybrooks/mgie
---
MGIE는 멀티모달 대형 언어 모델(MLLM)을 활용해 자연어로 된 간단한 지시문을 기반으로 이미지 편집을 개선하는 프로젝트입니다. 기존 방법의 한계를 극복하기 위해 MLLM이 생성된 표현을 풍부하게 변환하고 편집 모델에 시각적 상상력을 부여하는 엔드투엔드 학습 프레임워크를 제안합니다. ICLR 2024에서 스포트라이트로 선정된 이 연구는 LLaVA 코드베이스를 확장하여 구현되었으며, HuggingFace의 Vicuna-7B 및 LLaVA-7B 모델과 호환됩니다. 데이터 전처리, 학습, 추론 파이프라인을 포함하며, 데모 및 학습 스크립트를 제공합니다.