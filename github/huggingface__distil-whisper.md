---
Language: Python  
tags:  
 - Speech Recognition  
 - Whisper  
 - Distillation  
 - ASR  
 - HuggingFace  
aliases:  
 - Distil-Whisper  
 - Whisper 경량화  
 - 영어 음성 인식  
url: https://github.com/huggingface/distil-whisper/blob/main/README.md  
---  
Distil-Whisper는 영어 음성 인식을 위한 Whisper 모델의 경량화 버전입니다. 6배 빠른 추론 속도, 49% 더 작은 모델 크기, 1% 이내의 단어 오류율(WER)로 최적의 성능을 제공합니다. 주요 모델은 `distil-large-v3`이며, 메모리 제약이 있는 환경에서는 166M 파라미터의 `distil-small.en`을 추천합니다. 다국어 지원이 필요한 경우 Whisper Turbo를 권장합니다. Hugging Face Transformers 라이브러리와 호환되며, 다양한 사용 사례에 맞춰 유연하게 적용할 수 있습니다.  

> [!NOTE]  
> Distil-Whisper는 영어 전용 모델입니다. 다국어 음성 인식에는 Whisper Turbo를 사용하시기 바랍니다.