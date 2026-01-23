---
Language: Python  
tags:  
 - 오디오_전사  
 - Whisper  
 - CLI_도구  
 - GPU_가속  
 - HuggingFace  
aliases:  
 - insanely-fast-whisper  
 - 초고속_음성_전사  
 - 휘스퍼_고속화  
url: https://github.com/reach-vb/insanely-fast-whisper  
---  
이 프로젝트는 Hugging Face의 Transformers, Optimum, Flash Attention 2 기술을 활용해 오디오 파일을 초고속으로 전사할 수 있는 CLI 도구입니다. NVIDIA GPU 및 Apple Silicon(Mac)에서 작동하며, Whisper Large v3 모델로 2.5시간 분량의 음성을 약 98초 내에 처리할 수 있습니다. 다양한 최적화 기술(FP16, 배치 처리, Flash Attention 2)을 지원하며, 화자 분리(diarization) 기능도 포함되어 있습니다. 커뮤니티 주도로 개발되었으며, PyTorch 및 Hugging Face 생태계와의 통합이 용이합니다.