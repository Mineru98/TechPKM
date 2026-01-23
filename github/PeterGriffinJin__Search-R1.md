---
Language: Python  
tags:  
 - 강화학습  
 - LLM  
 - 검색엔진  
 - 툴사용  
 - 오픈소스  
aliases:  
 - Search-R1  
 - 검색추론LLM  
 - verL기반  
url: https://github.com/PeterGriffinJin/Search-R1  
---
Search-R1은 강화학습 프레임워크를 통해 추론과 검색엔진 호출을 번갈아 수행하는 LLM을 훈련시키는 오픈소스 프로젝트입니다. DeepSeek-R1과 OpenAI DeepResearch의 대안을 제공하며, PPO/GRPO 등 다양한 RL 방법과 Llama3/Qwen2.5 등 소형 기반 모델을 지원합니다. 로컬/온라인 검색엔진과 연동해 다단계 추론과 검색 능력을 학습시키며, 실험 로그와 논문(arXiv)을 통해 방법론과 결과를 공유합니다.  

핵심 기술 스택: Python, HuggingFace, Pytorch, vLLM, FlashAttention2  
주요 기능: 다중 검색엔진 지원, 멀티노드 훈련, 사용자 정의 데이터셋/코퍼스 통합 가능