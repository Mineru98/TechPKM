---
Language: Python
tags:
 - vllm
 - mcqa
 - 금융
 - 회계
 - 다중선택답변
aliases:
 - vllm-mcqa
 - 다중선택질문답변
 - 금융문제답변생성
 - K-IFRS
url: https://github.com/사용자명/vllm-mcqa
---
이 프로젝트는 VLLM 모델을 활용하여 다중선택질문(MCQA)에 대한 강제적인 답변 출력을 구현하는 간단한 코드입니다. 금융 회계 분야(예: K-IFRS)의 객관식 문제에 대해 A/B/C/D 형식의 제한된 답변 생성을 목표로 합니다. 로그 확률 제한과 허용 토큰 필터링을 통해 정확한 선택지 출력을 강제화하는 것이 핵심 특징입니다. Python 기반으로 구현되었으며, 'facebook/opt-1.3b' 같은 경량 모델에 적용 가능합니다.