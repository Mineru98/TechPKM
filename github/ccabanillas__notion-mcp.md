---
Language: Python  
tags:  
 - Notion 통합  
 - MCP 서버  
 - AI 연동  
 - 파이썬  
 - 앤트로픽 클로드  
aliases:  
 - Notion MCP 서버  
 - Notion 앤트로픽 연동  
 - MCP 1.6.0 서버  
 - Notion API 클라이언트  
url: https://github.com/ccabanillas/notion-mcp  
---  
이 프로젝트는 Notion API와 호환되는 Model Context Protocol(MCP) 서버를 구현하여 Claude Desktop 및 기타 MCP 클라이언트에서 Notion 데이터를 표준화된 방식으로 접근할 수 있도록 합니다. 비동기/await 지원, Pydantic v2 기반 타입 안전성, 상세한 로깅 및 오류 처리가 특징이며, 데이터베이스 조회, 페이지 생성, 검색 등의 핵심 기능을 제공합니다.  

주요 기술 스택은 Python이며, 앤트로픽 클로드와의 연동을 최적화했습니다. Notion 통합 토큰을 기반으로 동작하며, 데이터베이스 공유 권한 관리를 통해 접근 제어가 가능합니다. MCP 1.6.0 사양을 준수하여 호환성을 유지합니다.