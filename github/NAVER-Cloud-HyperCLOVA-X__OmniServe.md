---
Language: Python  
tags:  
 - 멀티모달  
 - LLM 추론  
 - Docker  
 - OpenAI API 호환  
 - 분산 처리  
aliases:  
 - OmniServe  
 - HyperCLOVAX-SEED 추론 시스템  
 - 멀티모달 LLM 서버  
url: https://github.com/NAVER-Cloud-HyperCLOVA-X/OmniServe  
---  
OmniServe는 이미지, 비디오, 오디오를 이해하고 생성할 수 있는 멀티모달 LLM 추론 시스템입니다. HyperCLOVAX-SEED 모델을 지원하며 OpenAI 호환 API를 제공하여 텍스트, 이미지, 오디오 간 변환이 가능한 엔드투엔드 서비스를 구축합니다. 멀티-GPU 분산 아키텍처와 Docker 기반 배포를 통해 확장성과 사용 편의성을 갖추었습니다.  

주요 특징으로는 △이미지/비디오 → 텍스트(VLM) 및 양방향 멀티모달(OMNI) 처리 △추론 모드 지원 △Docker Compose를 통한 간편한 설치 등이 있습니다. VLM(32B)과 OMNI(8B) 모델 중 필요에 따라 선택적으로 구동할 수 있습니다.