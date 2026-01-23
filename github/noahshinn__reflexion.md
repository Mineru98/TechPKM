---
Language: Python  
tags:  
 - Verbal Reinforcement Learning  
 - Language Agents  
 - ReAct Framework  
 - HotPotQA  
 - AlfWorld  
aliases:  
 - Reflexion 언어 에이전트  
 - 언어 강화학습  
 - Reflexion 논문 구현  
 - 언어 모델 자기 반성  
 - Verbal RL  
url: https://github.com/noahshinn/reflexion  
---  
이 프로젝트는 NeurIPS 2023에 발표된 "Reflexion: 언어 에이전트용 구두 강화학습" 논문의 공식 구현체입니다. 언어 모델이 자기 반성(self-reflection)을 통해 이전 시도에서 학습하며 성능을 개선하는 메커니즘을 연구하며, HotPotQA(추론), AlfWorld(의사결정), 프로그래밍 문제 해결 등의 벤치마크에서 실험할 수 있는 코드와 로그를 제공합니다. ReAct 프레임워크 기반의 에이전트 유형과 다양한 반성 전략(REFLEXION, LAST_ATTEMPT 등)을 구현한 것이 핵심 특징입니다. GPT-4 API 기반 실험 재현이 가능하나, 높은 비용 부담으로 인해 논문에서 사용한 모든 결과 로그가 제공됩니다.