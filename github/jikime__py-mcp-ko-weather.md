---
Language: Python
tags:
 - MCP 서버
 - 기상 데이터
 - 한국 날씨
 - KMA API
 - LLM 통합
aliases:
 - 한국 날씨 MCP 서버
 - py-mcp-ko-weather
 - Korea Weather MCP Server
url: https://github.com/jikime/py-mcp-ko-weather
---
이 프로젝트는 한국기상청(KMA) API를 기반으로 한 MCP(Multi-platform Communication Protocol) 서버로, 한국 지역별 정밀한 날씨 예보 정보를 제공합니다. 서울특별시 서초구 양재1동과 같은 세부 행정구역 단위까지 좌표 기반 예보를 지원하며, 온도, 강수확률, 습도 등 종합 기상 데이터를 구조화된 텍스트 형식으로 반환합니다. LLM(대형 언어 모델) 통합을 최적화한 응답을 제공하는 것이 핵심 특징입니다.  

### 주요 기능
- 한국 행정구역(시/구/동)별 정밀 그리드 좌표 조회
- 초단기 날씨 예보 및 시간별 상세 데이터 제공
- MCP 프로토콜을 통한 AI 에이전트 통합 지원
- KMA API 인증 기반 데이터 수집 시스템

> MIT 라이선스로 배포되며 Docker, 수동 설치 등 유연한 배포 방식을 지원합니다.