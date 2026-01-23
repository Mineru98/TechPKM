---
Language: Python
tags:
 - 대규모 언어 모델
 - 메모리 최적화
 - LLM 추론
 - GPU 효율화
 - 오픈소스 모델
aliases:
 - AirLLM
 - 4GB GPU에서 70B LLM 실행
 - AirLLM 메타데이터
 - 저사양 GPU LLM
url: https://github.com/lyogavin/airllm
---
AirLLM은 4GB GPU 카드에서 양자화, 증류, 가지치기 없이도 70B 규모의 대형 언어 모델 추론을 가능하게 하는 프로젝트입니다. 8GB VRAM 환경에서도 405B Llama3.1 모델 실행이 가능하며, 다양한 오픈소스 모델(ChatGLM, QWen, Baichuan 등)을 지원합니다. 레이어 분할 기술과 압축 기법(4/8비트 양자화)을 결합해 메모리 사용량을 최적화하면서도 최대 3배의 추론 속도 향상을 달성했습니다. MacOS 환경에서도 Apple 실리콘 기반 장치에서의 실행이 지원됩니다.