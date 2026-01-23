---
Language: Python  
tags:  
 - 주식 데이터  
 - KRX  
 - Playwright  
 - API 통합  
 - 금융 분석  
aliases:  
 - kospi-kosdaq-stock-server  
 - KRX 주식 서버  
 - 주식 데이터 서버  
url: https://github.com/dragon1086/kospi-kosdaq-stock-server  
---  
이 프로젝트는 KRX 데이터 마켓플레이스에서 KOSPI/KOSDAQ 주식 및 지수 데이터를 제공하는 MCP 서버입니다. Kakao OAuth 인증과 Playwright 기반 헤드리스 브라우저를 활용해 자동 세션 관리를 구현했으며, OHLCV 데이터, 시가총액, 재무제표, 투자자 유형별 거래량 등을 조회할 수 있습니다. 주요 기능으로는 주식 티커 검색, 역사적 가격 데이터, 지수 데이터(일간/월간/연간) 지원 등이 포함됩니다. Python 3.10+와 Kakao 계정이 필요하며, Docker를 통한 배포도 가능합니다.