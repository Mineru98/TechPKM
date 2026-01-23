---
Language: Python
tags:
 - LLM 추론
 - GPU 최적화
 - 로컬 LLM
 - Flash Attention
 - 양자화
aliases:
 - ExLlamaV2
 - 로컬 LLM 추론
 - EXL2 양자화
 - ExLlamaV2 동적 생성기
url: https://github.com/turboderp/exllamav2
---
ExLlamaV2는 현대 소비자 GPU에서 로컬로 대규모 언어 모델(LLM)을 실행하기 위한 추론 라이브러리입니다. Flash Attention 2.5.7 이상을 활용한 페이지 어텐션, 동적 배치 처리, 스마트 프롬프트 캐싱, K/V 캐시 중복 제거 등의 기능을 지원하며, 단순한 단일 생성부터 비동기 스트리밍 생성까지 다양한 생성 모드를 제공합니다. EXL2 양자화 포맷을 통해 2~8비트 양자화가 가능하며, 모델 내 양자화 수준을 혼합하여 성능을 최적화할 수 있습니다.  

TabbyAPI와 같은 호환 가능한 백엔드 서버를 통해 OpenAI 스타일의 API를 제공하며, 여러 웹 UI 및 텍스트생성 웹 인터페이스와 통합될 수 있습니다. PyPI를 통한 설치 또는 소스 빌드 방식으로 사용할 수 있으며, 다양한 모델 크기(7B~70B)와 양자화 모드를 지원합니다.