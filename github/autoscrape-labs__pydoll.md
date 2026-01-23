---
Language: Python  
tags:  
 - 웹자동화  
 - 스크래핑  
 - 비동기  
 - 봇회피  
 - 타입검사  
aliases:  
 - 피돌  
 - Pydoll  
 - 크롬디버그프로토콜  
 - 웹스크래핑  
url: https://github.com/autoscrape-labs/pydoll  
---  
Pydoll은 현대 웹 자동화 및 고성능 스크래핑을 위해 설계된 **이베이션(Evasion) 중심의 웹 자동화 프레임워크**입니다. Chrome DevTools Protocol(CDP)에 직접 연결하여 `webdriver` 탐지 없이 인간처럼 행동하는 자동화 환경을 제공하며, `async/await` 기반 네이티브 비동기 아키텍처와 100% 타입 검사를 지원합니다. UI 상호작용과 API 호출을 결합한 하이브리드 자동화, 네트워크 제어, 브라우저 핑거프린트 관리 등의 고급 기능을 통해 복잡한 안티봇 방어를 우회할 수 있습니다.  

주요 특징으로는 현실적인 인간 행동을 모방한 타이핑/스크롤, 요청 가로채기/모니터링, 브라우저 세션 기반의 API 호출, 멀티탭/컨텍스트 병렬 처리 등이 포함됩니다. Python 3.10+에서 사용 가능하며, 외부 의존성 없이 `pip install pydoll-python`으로 설치할 수 있습니다.  

[공식 문서](https://pydoll.tech/)에서 기술 심층 분석과 전략적 이베이션 가이드를 제공합니다.