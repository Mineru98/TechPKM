---
Language: Python
tags:
 - 음성인식(ASR)
 - 감정인식(SER)
 - 오디오판독(AED)
 - 딥러닝
 - FunASR
aliases:
 - SenseVoice
 - SenseVoiceSmall
 - 음성 기초 모델
url: https://github.com/FunAudioLLM/SenseVoice/blob/main/README.md
---
SenseVoice는 고정밀 다국어 음성 인식, 화자의 감정 인식, 오디오 이벤트 감지 기능을 통합적으로 제공하는 음성 기초 모델(Foundation Model)입니다. 50개 이상의 언어를 지원하며 비자율적(Non-autoregressive) 엔드투엔드 프레임워크를 채택해 기존 모델보다 15배 빠른 추론 속도(10초 오디오 처리 70ms)를 자랑합니다. 이 프로젝트는 파인튜닝 스크립트, ONNX 및 Libtorch 내보내기 기능과 더불어 다중 동시 요청을 지원하는 서비스 배포 파이프라인까지 제공하여 실제 비즈니스 환경에 즉각적으로 적용할 수 있도록 돕습니다.