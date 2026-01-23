---
Language: Python  
tags:  
 - 음성합성  
 - 음성복제  
 - AI음성  
 - 음성생성  
aliases:  
 - BARK-AI-음성복제  
 - Bark-음성생성  
 - SERP-AI-음성합성  
url: https://github.com/suno-ai/bark  
---
BARK AI는 텍스트 기반 음성 생성 모델로, 사용자 정의 오디오 샘플을 활용한 음성 복제 기능을 제공합니다. 다양한 언어(영어, 독일어, 스페인어 등)를 지원하며, 억양, 감정, 음악 요소 등을 포함한 현실적인 음성을 생성할 수 있습니다. Jupyter 노트북 기반의 `clone_voice.ipynb` 및 `generate.ipynb`를 통해 음성 복제 및 텍스트 기반 음성 생성이 가능합니다.  

```python
# 예시 코드
from bark import generate_audio
audio_array = generate_audio("안녕하세요, 반갑습니다.")
```