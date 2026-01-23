---
Language: Python  
tags:  
 - JAX  
 - 음성 인식  
 - Whisper 모델  
 - 고속 처리  
 - TPU/GPU  
aliases:  
 - Whisper-JAX  
 - Whisper_JA  
 - Whisper_JAX  
url: https://github.com/sanchit-gandhi/whisper-jax  
---  
이 프로젝트는 OpenAI의 Whisper 모델을 JAX 프레임워크로 최적화하여 구현한 리포지토리입니다. 기존 PyTorch 구현 대비 최대 70배 빠른 처리 속도를 제공하며, CPU, GPU, TPU 환경에서 호환됩니다. 주요 특징으로는 배치 처리, 반정밀도(bfloat16/float16) 지원, 타임스탬프 생성, 다중 언어 인식 등이 포함됩니다. 허깅페이스 허브와 통합된 모델 가중치 및 배치 처리 최적화를 통해 대용량 오디오 파일의 효율적인 전사가 가능합니다. 사용 사례로는 클라우드 TPU에서의 초고속 음성 변환, 실시간 전사 엔드포인트 구축 등이 있습니다.