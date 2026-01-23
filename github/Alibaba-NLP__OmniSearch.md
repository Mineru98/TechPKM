---
Language: Python  
tags:  
 - 멀티모달 RAG  
 - 자기적응 계획 에이전트  
 - VQA 데이터셋  
 - PyTorch  
 - MLLM  
aliases:  
 - OmniSearch  
 - Dyn-VQA  
 - 멀티모달 RAG 에이전트  
 - 동적 VQA  
url: https://github.com/Alibaba-NLP/OmniSearch  
---
OmniSearch는 질문 해결 단계와 현재 검색 내용에 따라 실시간으로 검색 작업을 계획하는 최초의 자기적응 멀티모달 RAG 에이전트입니다. 실제 질문 환경에서 동적 지식 검색 요구사항을 반영한 Dyn-VQA 데이터셋을 제안하며, 다양한 MLLMs의 성능을 벤치마크합니다. 이 프로젝트는 PyTorch 기반의 멀티모달 검색 증강 생성 기술을 발전시키고, GPT-4V 및 Qwen-VL 모델과의 통합 사례를 제공합니다.  

핵심 기술 스택은 Python, PyTorch, 멀티모달 LLM이며, 모델 훈련 및 평가를 위한 상세한 가이드와 데이터셋 구조를 포함하고 있습니다. 연구 논문(arXiv:2411.02937)과 데모(https://alibaba-nlp.github.io/OmniSearch/)를 통해 추가 정보를 확인할 수 있습니다.