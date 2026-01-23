---
Language: Python  
tags:  
 - 실시간 음성-텍스트 변환  
 - Apple Silicon 최적화  
 - MLX 프레임워크  
 - CoreML 가속화  
 - 동시성 음성 인식  
aliases:  
 - Lightning-SimulWhisper  
 - 실시간 자막 생성기  
 - 애플 기기용 고속 음성 인식  
url: https://github.com/altalt-org/Lightning-SimulWhisper  
---  
Lightning-SimulWhisper는 Apple Silicon 기기에서 실시간 로컬 음성-텍스트 변환을 최적화하는 프로젝트입니다. MLX 프레임워크와 CoreML 가속화를 결합해 최대 18배 빠른 인코딩 및 15배 빠른 디코딩 성능을 제공하며, AlignAtt 정책을 활용한 동시성 음성 인식 기능을 구현했습니다. 주요 특징은 CoreML 인코더 기반의 전력 효율성과 다양한 Whisper 모델 지원입니다.  

이 프로젝트는 PyTorch 의존성을 제거하고 Apple Neural Engine을 활용한 하드웨어 가속화로 데스크톱 및 모바일 기기에서의 실시간 자막 생성에 최적화되었습니다.