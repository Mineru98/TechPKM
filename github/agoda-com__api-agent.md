---
Language: Python
tags:
 - MCP
 - API
 - GraphQL
 - REST
 - LLM
aliases:
 - API Agent
 - MCP Server Generator
url: https://github.com/agoda-com/api-agent
---
이 프로젝트는 GraphQL 또는 REST API를 가리켜 자연어로 질문할 수 있는 MCP(Model Context Protocol) 서버로 변환해주는 도구입니다. OpenAI Agents SDK와 DuckDB를 활용하여, API가 지원하지 않는 정렬, 필터링, 조인 등의 작업을 데이터를 수집 후 SQL 후처리를 통해 구현합니다. 또한 성공한 쿼리를 재사용 가능한 레시피로 캐싱하여 효율성을 높이는 것이 특징입니다.