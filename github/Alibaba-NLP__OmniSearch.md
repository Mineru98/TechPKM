---
Language: Python
tags:
 - Multimodal RAG
 - Planning Agent
 - VQA 데이터셋
 - MLLM 벤치마킹
 - 동적 검색
aliases:
 - OmniSearch
 - 동적 VQA
 - 다모달 RAG
- 자기적응 에이전트
url: https://github.com/Alibaba-NLP/OmniSearch
---
OmniSearch는 질문 해결 단계와 검색 내용에 따라 실시간으로 검색 액션을 계획하는 자기적응형 다모달 RAG(에이전트)입니다. 기존 mRAG 벤치마크의 한계를 극복하기 위해 동적 검색 요구 사항을 반영한 Dyn-VQA 데이터셋을 제안하며, 다양한 MLLM(다모달 대형 언어 모델)의 성능을 벤치마킹합니다. 이 프로젝트는 PyTorch 기반으로 구현되었으며, GPT-4V 및 Qwen-VL 기반 실행 환경을 지원합니다. 주요 기술 스택은 Python이며, 검색 증강을 통한 질문 답변 시스템 개발에 중점을 둡니다.