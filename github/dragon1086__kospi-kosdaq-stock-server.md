---
Language: Python
tags:
 - 주식 데이터
 - KRX
 - 금융 분석
 - Python 패키지
 - MCP 서버
aliases:
 - KRX 주식 서버
 - 코스닥 주식 서버
 - 코스피 주식 서버
 - kospi-kosdaq-stock-server
url: https://github.com/dragon1086/kospi-kosdaq-stock-server
---
이 프로젝트는 KRX 데이터 마켓을 통해 코스피/코스닥 주식 데이터를 제공하는 MCP 서버입니다. 카카오 OAuth 인증과 Playwright 기반 헤드리스 브라우저를 활용해 직접 KRX API에 접근하며, 주식 시세, 시가총액, 펀더멘털 데이터, 투자자 유형별 거래량, 지수 데이터 등을 조회할 수 있습니다. 세션 자동 관리 및 재로그인 기능을 지원합니다.  

주요 기능:  
- 티커 조회(코스피/코스닥)
- OHLCV(시가/고가/저가/종가/거래량) 데이터
- 시가총액, PER/PBR/배당률, 투자자 유형별 거래량
- KOSPI/KOSDAQ 지수 데이터  

요구사항: Python 3.10+, 카카오 계정(2FA 비활성화), Playwright Chromium 브라우저.