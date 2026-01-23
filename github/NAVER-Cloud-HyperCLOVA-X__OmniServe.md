---
Language: Python  
tags:
 - 인공지능
 - 멀티모달
 - 추론 시스템
 - OpenAI 호환
 - Docker  
aliases:
 - OmniServe
 - 네이버 하이퍼클로바 X
 - 멀티모달 LLM  
url: https://github.com/NAVER-Cloud-HyperCLOVA-X/OmniServe  
---
OmniServe는 텍스트, 이미지, 비디오, 오디오를 처리하는 멀티모달 LLM 추론 시스템입니다. HyperCLOVAX-SEED 모델을 지원하며 OpenAI 호환 API와 분산 GPU 추론을 제공합니다. Docker 기반 배포와 체인 오브 사고(Chain-of-Thought) 추론 모드 등 다양한 기능을 포함하며, VLM(비전 언어 모델)과 OMNI(멀티모달 모델) 아키텍처를 기반으로 합니다.  

이 시스템은 이미지/비디오/오디오 입력과 텍스트/이미지/오디오 출력을 모두 처리할 수 있으며, S3 연동을 통한 이미지/오디오 생성이 가능합니다. vLLM 기반의 고성능 LLM 서버와 인코더/디코더 모듈이 결합된 분산 아키텍처로 설계되었습니다.