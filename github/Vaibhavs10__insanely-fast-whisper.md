---
Language: Python  
tags:  
 - Whisper  
 - 음성-텍스트 변환  
 - GPU 최적화  
 - CLI 도구  
 - HuggingFace  
aliases:  
 - insanely-fast-whisper  
 - 초고속 Whisper  
 - 빠른 음성 변환  
 - Flash Attention 2  
url: https://github.com/Vaibhavs10/insanely-fast-whisper  
---  
**Insanely Fast Whisper**는 NVIDIA GPU 또는 Apple Silicon(Mac)에서 Whisper 모델을 활용해 오디오 파일을 초고속으로 텍스트로 변환하는 CLI 도구입니다. Hugging Face의 Transformers, Optimum, Flash Attention 2 기술을 결합해 2.5시간 분량의 오디오를 약 2분 만에 처리할 수 있습니다. 사용자는 다양한 Whisper 모델(예: large-v3, distil-large-v2)과 배치 크기, Flash Attention 2 옵션 등을 선택해 성능을 최적화할 수 있습니다.  

Whisper-large-v3 모델로 150분 오디오를 처리하는 데 약 1분 38초, distil-large-v2 모델로는 약 1분 18초가 소요됩니다. CLI를 통해 설치 및 사용이 간편하며, Windows, Mac, Colab 환경 등에서 동작합니다. 추가적으로 화자 분리(Diarization) 기능도 지원합니다.