---
Language: Python  
tags:  
 - RAG  
 - Model Context Protocol  
 - LLM 통합  
 - 파일 관리  
 - API 서버  
aliases:  
 - Storm MCP Server  
 - Sionic AI RAG 서버  
 - MCP 프로토콜 구현  
 - Storm Platform 연동  
url: https://github.com/sionic-ai/storm-mcp-server  
---  
이 프로젝트는 Anthropic의 Model Context Protocol(MCP)을 구현하여 LLM 애플리케이션과 RAG 데이터 소스/도구 간 통합을 가능하게 하는 서버입니다. Sionic AI의 Storm Platform과 연동해 임베딩 모델 및 벡터DB를 활용할 수 있으며, 파일 업로드, 도구 호출, API 통합 등의 기능을 제공합니다. Claude Desktop에서 직접 사용 가능한 MCP 서버로, Python 기반 서버리스 아키텍처를 채택했습니다.