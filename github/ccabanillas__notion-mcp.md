---
Language: Python  
tags:  
 - Notion 통합  
 - MCP 프로토콜  
 - AI 보조 도구  
 - async/await  
 - Pydantic  

aliases:  
 - notion-mcp  
 - notion-mcp-server  
 - notion-mcp-서버  
 - notion-mcp-메타데이터  

url: https://github.com/ccabanillas/notion-mcp/blob/main/README.md  
---  
Notion MCP 서버는 Notion API와 상호작용하기 위한 표준화된 MCP(Model Context Protocol) 인터페이스 구현체입니다. Claude Desktop 및 기타 MCP 클라이언트와의 호환성을 제공하며, Notion 데이터베이스 쿼리, 페이지 생성/수정, 검색, 블록 자식 정보 조회 등의 기능을 비동기(async/await) 및 타입 세이프(Pydantic v2) 방식으로 지원합니다.  

이 프로젝트는 Notion 통합 토큰을 사용해 설정되며, Smithery를 통한 자동 설치 또는 수동 설치 방식으로 배포 가능합니다. 주요 사용 사례는 AI 보조 도구와의 연동으로, Notion 데이터 관리에 특화된 MCP 서버 역할을 수행합니다.