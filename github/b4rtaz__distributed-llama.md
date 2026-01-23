---
Language: Python/C++
tags:
 - 분산_추론
 - LLM_최적화
 - 텐서_병렬화
 - 크로스플랫폼
 - 오픈소스
aliases:
 - dist-llama
 - 분산_라마
 - 분산_LLM_추론
 - dllama
url: https://github.com/b4rtaz/distributed-llama
---
분산 라마는 이더넷 기반의 고속 동기화를 통해 여러 홈 장치를 연결하여 LLM 추론 속도를 가속화하는 프로젝트입니다. 텐서 병렬화를 활용하여 장치 수가 증가할수록 성능이 향상되며, Linux/macOS/Windows와 ARM/x86_64 AVX2 아키텍처를 모두 지원합니다. Q40 양자화 모델을 기반으로 Llama 3 시리즈 및 Qwen 3 시리즈 등 다양한 모델을 실행할 수 있습니다.  

주요 특징은 단일 명령어로 루트 노드 설정, 수동 모델 변환, 2^n 노드 구성 최적화 등이 있으며, CLI 채팅, API 서버, 벤치마크 추론 기능을 제공합니다. RAM 사용량을 줄이기 위해 시퀀스 길이 제한 등의 옵션을 지원합니다. MIT 라이선스로 배포되는 오픈소스 프로젝트입니다.