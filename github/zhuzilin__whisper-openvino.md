---
Language: Python  
tags:  
 - 음성 인식  
 - Whisper 모델  
 - OpenVINO  
 - ASR(Automatic Speech Recognition)  
 - 성능 최적화  
aliases:  
 - whisper-openvino  
 - Whisper OpenVINO 백엔드  
 - openvino-whisper  
 - Whisper OpenVINO 변환  
url: https://github.com/zhuzilin/whisper-openvino  
---  
이 프로젝트는 OpenVINO 백엔드로 변환된 Whisper 음성 인식(ASR) 모델 포크로, `large` 모델을 제외한 모든 모델의 음성 변환 기능을 지원합니다. 기존 Whisper와 동일한 사용법으로 인텔 기반 하드웨어에서 추론 성능을 크게 개선할 수 있으며, 벤치마크 결과 92분 길이의 오디오 처리 시간을 67.57분에서 39.16분으로 단축했습니다. OpenVINO를 활용해 효율적인 음성 인식 파이프라인을 구현합니다.