---
Language: Python  
tags:  
 - 음성 인식 모델  
 - OpenVINO 최적화  
 - Whisper 모델  
 - 실시간 ASR  
 - ONNX 변환  
aliases:  
 - Whisper-OpenVINO  
 - whisper-openvino  
 - OpenVINO Whisper  
 - Whisper ASR 최적화  
url: https://github.com/zhuzilin/whisper-openvino  
---  
이 프로젝트는 Whisper 음성 인식 모델을 OpenVINO 백엔드로 최적화한 포크입니다. `large` 모델을 제외한 모든 모델의 음성 인식(transcribe) 기능을 지원하며, 기존 Whisper과 동일한 사용법으로 2배 이상의 성능 향상을 제공합니다. CPU 중심 환경에서도 효율적인 실시간 음성 인식이 가능하며, ONNX 변환 가중치는 허깅페이스 모델 허브에 공개되어 있습니다.  

> 핵심 기능:  
> - OpenVINO 기반 추론 가속  
> - 기존 Whisper과 호환되는 인터페이스  
> - `tiny`, `base`, `small` 모델 지원  
> - 92분 음성 처리 시 39.16분(기존 대비 42% 속도 개선)  
> - ONNX 모델 배포 지원