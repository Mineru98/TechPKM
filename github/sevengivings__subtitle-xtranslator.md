---
Language: Python  
tags:  
 - 자막 번역  
 - 음성 인식  
 - Google Cloud  
 - DeepL  
 - AI 번역  
aliases:  
 - subtitle-xtranslator  
 - 자막 추출 번역기  
 - Python 자막 처리  
url: https://github.com/sevengivings/subtitle-xtranslator  
---  
이 프로젝트는 동영상/오디오 파일에서 자막을 추출하고 Google Cloud Translation, DeepL API 등을 활용해 번역하는 Python 스크립트입니다. OpenAI Whisper, stable-ts, faster-whisper 기반의 음성 인식 기술과 통합되어 있으며, 반복 자막 제거, 짧은 자막 필터링 등의 기능을 제공합니다. 윈도우 및 Colab 환경에서 활용 가능하며, GPU 가속화 및 WebUI(Gradio) 인터페이스를 지원합니다.  

> **핵심 기술**:  
> - 음성 인식: Whisper, stable-ts, faster-whisper  
> - 번역: Google Cloud Translation, DeepL  
> - 자막 처리: 중복/짧은 자막 제거, SRT 형식 지원  
> **주요 기능**:  
> - 단일/다중 파일 처리  
> - WebUI(Gradio)를 통한 실시간 모니터링  
> - 환경 변수를 통한 API 키 관리  
> - GPU 최적화 및 Quantization 지원 (int8/cuBLAS)  

> **제한 사항**:  
> - 음성 인식의 정확도 한계  
> - 유료 번역 API 사용 시 비용 발생 가능성  
> - 고사양 GPU 요구 (특히 Demucs/VAD 사용 시)