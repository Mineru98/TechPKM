---
Language: Python
tags:
 - LLM
 - 추론 엔진
 - 오프로딩
 - 처리량 최적화
 - GPU 메모리
aliases:
 - FlexLLMGen
 - 플렉스엘엘엠젠
 - LLM 오프로딩 추론
url: https://github.com/FMInference/FlexLLMGen/blob/main/README.md
---
FlexLLMGen은 메모리가 제한된 단일 GPU 환경에서 대규모 언어 모델의 높은 처리량을 달성하기 위한 생성 추론 엔진입니다. IO 효율적인 오프로딩, 압축, 대규모 배치 처리를 통해 지연 시간보다는 처리량이 중요한 백그라운드 작업(벤치마킹, 데이터 랭글링 등)에 최적화되어 있습니다. GPU, CPU, 디스크의 자원을 유연하게 결합하여 비용이 저렴한 상용 GPU에서도 대형 모델을 실행할 수 있도록 지원합니다.