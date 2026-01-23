---
Language: Python  
tags:  
 - 암호화폐  
 - API 래퍼  
 - 업비트  
 - 금융 데이터 분석  
 - 파이썬 라이브러리  
aliases:  
 - pyupbit  
 - 업비트 API 파이썬  
 - 암호화폐 시세 분석  
url: https://github.com/sharebook-kr/pyupbit  
---
pyupbit은 업비트 API를 파이썬에서 편리하게 사용할 수 있도록 만든 래퍼 라이브러리입니다. 암호화폐 시세 조회, 차트 데이터 분석, 매수/매도 주문 등 업비트 거래 기능을 프로그래밍적으로 활용할 수 있습니다. `get_tickers`로 암호화폐 목록을, `get_current_price`로 실시간 시세를 확인하며, `get_ohlcv`로 캔들스틱 데이터를 DataFrame 형태로 얻을 수 있습니다. 또한 로그인 인증을 통해 실제 주문, 잔고 조회, 미체결 주문 취소 등 거래소 API 기능도 지원됩니다. 웹소켓을 통해 실시간으로 체결, 호가 정보를 수신할 수 있어 자동화 트레이딩 시스템 구축에 적합합니다.