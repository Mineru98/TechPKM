---
Language: Python
tags:
 - MCP
 - MySQL
 - AI
 - 데이터베이스
 - 파이썬
aliases:
 - mysql-mcp-server
 - MCP-MySQL
 - MySQL MCP 서버
 - MCP 서버
 - AI-MySQL
url: https://github.com/Mineru98/mysql-mcp-server
---
MCP MySQL 서버는 MCP(Model Context Protocol) 기반의 MySQL 데이터베이스 운영 서버입니다. AI 모델이 MySQL 데이터베이스와 상호작용할 수 있도록 테이블 생성/조회, 쿼리 실행, 시각화 추천 등의 도구를 제공합니다. Docker, Python 기반으로 배포 가능하며, Cursor IDE v0.46 이상과 연동해 사용할 수 있습니다.

### 주요 특징
- **MCP 프로토콜**을 통한 AI 모델과의 통신
- **MySQL 8.0** 및 **Python 3.x** 기반 구현
- **FastMCP** 서버, **PyMySQL**, **pandas** 활용
- Docker/Docker Compose를 통한 컨테이너화 지원
- 확장 가능한 툴셋 구조(`executors/` 디렉토리 기반)

### 핵심 기능
- 테이블 스키마 조회(desc_table)
- SQL 실행 계획 분석(explain)
- SELECT/INSERT 쿼리 실행
- 시각화 차트 추천(invoke_viz_pro)
- 보고서 생성(insight_starter)