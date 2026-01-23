---
Language: Python  
tags:  
 - MySQL  
 - MCP 프로토콜  
 - AI 데이터베이스 통합  
 - Docker 배포  
 - 데이터 시각화  
aliases:  
 - mysql-mcp-server  
 - MCP MySQL 서버  
 - AI MySQL 통합 서버  
url: https://github.com/Mineru98/mysql-mcp-server  
---
MCP MySQL 서버는 Model Context Protocol(MCP) 기반의 MySQL 데이터베이스 연동 서버입니다. AI 모델이 데이터베이스 작업을 수행할 수 있도록 도구 세트를 제공하며, 테이블 생성, 쿼리 실행, 스키마 분석, 시각화 추천 등 다양한 기능을 지원합니다. Python으로 구현되었으며 Docker를 통한 배포와 직접 실행이 가능합니다.  

주요 기술 스택은 MySQL 8.0, FastMCP, PyMySQL 등이며, `executors` 디렉토리에 도구별 실행 모듈을 분리하여 확장성을 확보했습니다. Cursor Pro 계정과 연동해 AI 개발 환경에서 MCP 기능을 활용할 수 있습니다.