---
Language: Python
tags:
 - vllm
 - mcqa
 - logits_processing
 - 한국어
 - 금융
aliases:
 - vllm-mcqa
 - 다중선택답변생성
 - vllm_강제선택출력
url: https://github.com/guijinSON/vllm-mcqa
---
vLLM에서 다중선택형 질문(MCQA)에 대한 강제 답변 출력을 구현한 프로젝트입니다. 금융회계 분야의 객관식 문제 해결을 위해 'A/B/C/D' 옵션 중 단일 토큰 출력을 유도하는 로직을 포함합니다. 허가된 토큰 ID 필터링과 로짓 처리 기술을 활용해 답변 후보를 제한하며, 한국어 질문 처리에 최적화된 구조를 가집니다.