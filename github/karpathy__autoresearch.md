---
Language: Python
tags:
 - LLM
 - AutonomousAgents
 - AIResearch
 - ExperimentAutomation
 - PyTorch
aliases:
 - 오토리서치
 - Karpathy AutoResearch
 - 자율 연구 에이전트
url: https://github.com/karpathy/autoresearch
---

이 프로젝트는 Andrej Karpathy가 제안한 실험적인 자율 연구 시스템으로, AI 에이전트가 LLM 학습 코드를 자율적으로 수정하고 실험하여 모델을 개선하는 것을 목표로 합니다. 사용자는 `train.py`를 수정하는 에이전트를 제어하는 `program.md`를 편집하여 연구 방향을 설정하며, 에이전트는 5분의 시간 제한 내에 스스로 코드를 변경하고 결과를 검증하는 과정을 밤새 반복합니다. 단일 GPU 환경에서 작동하도록 설계된 이 시스템은 코드 자체를 수정하는 방식을 통해 연구 자동화와 탐색적 학습을 가능하게 합니다.