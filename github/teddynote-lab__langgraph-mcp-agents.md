---
Language: Python  
tags:  
 - LangGraph  
 - MCP  
 - ReAct Agent  
 - Streamlit  
 - AI Agent  
aliases:  
 - LangGraph-MCP-Agents  
 - LangChain-MCP-Adapters  
 - MCP 도구 관리  
 - ReAct 에이전트  
 - LangGraph MCP 통합  
url: https://github.com/teddylee777/langgraph-mcp-agents  
---
이 프로젝트는 LangChain AI의 MCP(Model Context Protocol) 어댑터를 활용해 외부 도구와 데이터 소스에 접근할 수 있는 ReAct 에이전트를 Streamlit 인터페이스로 배포하는 도구입니다. MCP 서버를 통해 다양한 모델을 통합하며, 실시간 응답 스트리밍, 대화 기록 관리, 동적 도구 구성 기능이 특징입니다. Python 3.12 이상에서 동작하며 Docker 또는 직접 설치 방식으로 실행할 수 있습니다.  

주요 기술 스택은 LangGraph, Streamlit, Anthropic/Claude-3 및 OpenAI 모델이며, LangSmith 추적 기능을 지원합니다. 사용자는 Smithery 플랫폼에서 제공하는 JSON 구성으로 MCP 도구를 자유롭게 추가/관리할 수 있습니다. 핸즈온 튜토리얼(한글 Jupyter 노트북)을 통해 MCP 클라이언트 설정, RAG 통합, 혼합 전송 프로토콜 구현 방법을 배울 수 있습니다. MIT License로 배포됩니다.