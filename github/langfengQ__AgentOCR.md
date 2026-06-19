---
Language: Python
tags:
 - LLM Agent
 - OCR
 - Reinforcement Learning
 - Visual Token
 - Multi-turn
aliases:
 - AgentOCR
 - 에이전트 광학 문자 인식
 - Optical Self-Compression
url: https://github.com/langfengQ/AgentOCR/blob/master/README.md
---
AgentOCR는 다중 턴 LLM 에이전트 학습 시 급격히 증가하는 텍스트 기록의 병목 문제를 해결하기 위해, 관찰-행동 기록을 압축된 이미지로 렌더링하여 시각적 토큰으로 표현하는 프로젝트입니다. 시각적 토큰의 높은 정보 밀도를 활용해 토큰 소비량을 50% 이상 줄이면서도 95% 이상의 성능을 유지하며, 해시 기반 세그먼트 캐싱과 에이전트 자체 압축률 학습을 통해 효율성을 극대화합니다.