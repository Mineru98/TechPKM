---
Language: Python  
tags:  
 - RAG  
 - LLM  
 - Wikipedia  
 - Chatbot  
 - Hallucination-Reduction  
aliases:  
 - 위키챗  
 - WikiChat  
 - RAG 시스템  
url: https://github.com/stanford-oval/WikiChat  
---  
위키챗은 대규모 언어 모델(LLM)의 환각 현상을 줄이기 위해 위키피디아 기반의 7단계 파이프라인을 사용하는 챗봇 프로젝트입니다. 위키피디아 검색 API와 다양한 LLM(오픈AI, Anthropic, Mistral 등)을 통합하여 사실 기반의 응답을 생성하며, 다국어 지원 및 구조화된 데이터 처리 기능을 포함합니다. 위키챗은 로컬 또는 클라우드 환경에서 실행 가능하며, 멀티유저 배포를 위한 Chainlit 통합 및 Cosmos DB 연동 기능을 제공합니다.  

위키챗은 EMNLP 2023 및 ACL 2024 논문으로 발표되었으며, 위키미디어 연구상 수상 이력을 가진 프로젝트입니다. 주요 기능으로는 다국어 위키피디아 검색, 구조 데이터(테이블, 인포박스 등) 처리, 경량화된 추론 파이프라인, 그리고 사용자 시뮬레이션을 통한 평가가 포함됩니다.  

이 프로젝트는 Apache-2.0 라이선스로 공개되었으며, 로컬 LLM 배포 또는 클라우드 기반 API 연동을 통해 유연하게 사용 가능합니다.  

핵심 특징:  
- 25개 언어 위키피디아 지원  
- 다중 LLM 호환성 (LiteLLM 기반)  
- 구조화된 데이터 검색 및 처리  
- 가벼운 추론을 위한 증류 모델 옵션  
- 로컬/클라우드 배포 지원  
- 커뮤니티 및 연구용으로 무료 검색 API 제공