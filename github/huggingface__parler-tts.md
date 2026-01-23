---
Language: Python  
tags:  
 - Text-to-Speech  
 - 음성합성  
 - 오픈소스  
 - 딥러닝  
 - 허깅페이스  
aliases:  
 - Parler-TTS  
 - 패러러TTS  
 - 음성생성모델  
 - TTS 오픈소스  
url: https://github.com/huggingface/parler-tts  
---  
Parler-TTS는 특정 화자(성별, 피치, 발화 스타일 등)의 음성을 고음질로 생성할 수 있는 경량 오픈소스 텍스트-음성 변환(TTS) 모델입니다. Stability AI와 에든버러 대학의 연구 논문을 재현한 이 프로젝트는 데이터셋, 학습 코드, 가중치까지 모두 공개되어 커뮤니티가 자체 TTS 모델을 개발할 수 있도록 지원합니다. 45,000시간의 오디오북 데이터로 학습된 두 가지 버전(880M 파라미터 Mini 모델과 2.3B 파라미터 Large 모델)을 제공하며, SDPA 및 Flash Attention 2 최적화를 통해 빠른 생성이 가능합니다.  

주요 특징:  
1. 텍스트 프롬프트로 음성 특성 제어(예: "여성 화자의 약간 표현력이 있고 빠른 속도의 발음")  
2. 34명의 화자(목소리 특성 일관성 보장) 지원  
3. 고품질 오디오 생성에 최적화된 기술 적용  
4. 허깅페이스 생태계와 통합되어 쉽게 설치 및 사용 가능(`pip install git+https://github.com/huggingface/parler-tts.git`)