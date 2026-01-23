---
Language: Python  
tags:  
 - LangGraph  
 - Google Gemini  
 - 연구 증강형 AI  
 - 풀스택 애플리케이션  
 - 웹 검색 통합  
aliases:  
 - Gemini-LangGraph-퀵스타트  
 - 연구 기반 챗봇  
 - 랭크그래프 에이전트  
 - Gemini 기반 연구 도구  
url: https://github.com/langchain-ai/langgraph/tree/main/examples/gemini_fullstack  
---
이 프로젝트는 React 프론트엔드와 LangGraph 기반 백엔드 에이전트를 결합한 풀스택 애플리케이션입니다. 사용자의 질문에 대해 Google 검색 API를 활용한 동적 검색어 생성, 웹 연구, 지식 격차 분석을 통해 반복적으로 검색을 개선하며 인용이 포함된 답변을 제공하는 연구 증강형 대화형 AI를 구현합니다. Gemini 모델을 활용한 에이전트는 초기 쿼리 생성부터 최종 답변 합성까지 종합적인 연구 프로세스를 수행합니다.  

개발 환경에서는 핫리로딩을 지원하며, 프로덕션 배포 시 Redis와 Postgres 데이터베이스가 필요합니다. Docker 컴포즈를 통한 배포 옵션도 제공됩니다.