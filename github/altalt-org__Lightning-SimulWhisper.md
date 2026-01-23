---
Language: Python  
tags:  
 - Apple Silicon  
 - 실시간 음성 인식  
 - MLX Framework  
 - CoreML  
 - Whisper 모델  
aliases:  
 - Lightning-SimulWhisper  
 - 실시간 자막 생성  
 - 애플 기기 음성 인식  
 - 동시성 음성 전사  
url: https://github.com/altalt-org/Lightning-SimulWhisper  
---  
Lightning-SimulWhisper는 Apple Silicon 기기에서 최적의 성능을 제공하는 실시간 음성-텍스트 전환 프로젝트입니다. MLX 프레임워크와 CoreML을 활용해 인코더에서 최대 18배, 디코더에서 15배의 속도 향상을 달성하며, AlignAtt 정책을 사용해 동시성 스트리밍 인식을 구현합니다. 핵심 기술 스택은 Apple Neural Engine 기반의 CoreML 인코더와 MLX 디코더로 구성되어 있으며, 다양한 Whisper 모델 크기를 지원합니다. 전력 효율성과 실시간 처리 능력을 동시에 확보한 것이 특징입니다.