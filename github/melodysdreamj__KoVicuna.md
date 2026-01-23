---
Language: Python
tags:
 - 한국어 LLM
 - Vicuna
 - 한국어 번역 모델
 - LLaMA 7B
 - GPT 대화 모델
aliases:
 - KoVicuna
 - 한국어 Vicuna
 - KoVicuna7B
 - ko_vicuna
url: https://github.com/melodysdreamj/KoVicuna
---
KoVicuna는 Vicuna 모델을 기반으로 한국어 대화 데이터를 학습하여 개발된 한국어 LLM입니다. ShareGPT 데이터셋의 62만 대화문을 DeepL로 번역해 학습에 사용했으며, 8개의 A100 GPU로 15시간 동안 훈련되었습니다. 이 모델은 한국어 기반 대화형 AI 서비스 구현을 목적으로 하며, 허깅페이스에서 모델 가중치를 공개해 누구나 활용할 수 있습니다.  

주요 특징으로는 Vicuna 7B 기반 학습, GGML 형식 양자화 모델 지원, 코랩 데모 및 text-generation-webui 연동 기능이 포함됩니다. 학습은 주로 Python 환경에서 진행되었으며, 한국어 생성 및 이해 태스크에 최적화되어 있습니다.