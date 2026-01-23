---
Language: Python  
tags:  
 - KoCLIP  
 - 멀티모달 모델  
 - 한국어 NLP  
 - 이미지 인식  
 - HuggingFace  
aliases:  
 - KoCLIP 메타데이터  
 - 한국어 CLIP 모델  
 - koclip-base  
 - koclip-large  
url: https://github.com/jaketae/koclip  
---  
KoCLIP은 OpenAI의 CLIP 모델을 한국어에 맞게 포팅한 프로젝트입니다. MSCOCO 데이터셋의 한국어 번역 캡션을 활용해 훈련되었으며, 이미지와 텍스트 간의 의미적 유사성을 분석하는 멀티모달 모델입니다. `koclip-base`와 `koclip-large` 두 가지 버전이 제공되며, 각각 RoBERTa-large 언어 모델과 ViT 백본을 사용합니다. 한국어 쿼리뿐만 아니라 간단한 영어 단어에서도 작동하는 다국어 특성을 보입니다. Hugging Face 및 JAX 라이브러리를 통해 쉽게 로드하여 활용할 수 있습니다.