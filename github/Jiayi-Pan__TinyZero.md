---
Language: Python
tags:
 - 강화학습
 - 언어모델
 - 계산추론
 - 오픈소스
 - 재현연구
aliases:
 - TinyZero
 - DeepSeek R1 Zero 재현
 - 계산추론 강화학습
 - 소규모 언어모델
url: https://github.com/Jiayi-Pan/TinyZero
---
TinyZero는 [DeepSeek R1 Zero](https://github.com/deepseek-ai/DeepSeek-R1)의 계산 추론 기능(카운트다운 및 곱셈 작업)을 재현하는 오픈소스 프로젝트입니다. veRL 프레임워크를 기반으로 3B 규모 언어 모델에 강화학습을 적용하여 자체 검증 및 탐색 능력을 개발하며, 저비용(< $30)으로 실험 환경을 구축할 수 있도록 설계되었습니다. Qwen2.5 모델 시리즈를 활용하며, 병렬 추론 및 실험 로그 모니터링 기능을 통해 효율적인 연구를 지원합니다.