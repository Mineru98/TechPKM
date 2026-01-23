---
Language: Python  
tags:  
 - RAG  
 - 위키기반 AI  
 - 환각 방지  
 - LLM 최적화  
 - 다국어 검색  
aliases:  
 - 위키챗  
 - WikiChat  
 - 스탠포드 위키챗  
 - 환각 방지 챗봇  
 - 위키백과 기반 검색  
url: https://github.com/stanford-oval/WikiChat  
---  
WikiChat은 대규모 언어 모델(LLM)의 환각 현상을 방지하기 위해 위키백과의 정보를 활용하는 프로젝트입니다. 7단계 파이프라인을 통해 사실적 정확성을 보장하며, 다국어 위키백과 검색 API와 커스텀 인덱스 생성 기능을 제공합니다. 스탠포드 대학 연구진이 개발했으며, EMNLP 2023 논문 및 ACL 2024 후속 연구를 기반으로 합니다.  

주요 기능으로는 25개 언어 위키백과 검색, 구조화된 데이터(테이블/인포박스) 처리, LiteLLM을 통한 100개 이상의 LLM 호환성, Chainlit/Redis/Cosmos DB 기반의 멀티유저 배포 지원 등이 있습니다. 오픈소스로 공개되어 연구 및 상용 프로젝트에 활용 가능합니다.