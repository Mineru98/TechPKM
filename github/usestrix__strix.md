---
Language: Python  
tags:  
 - 보안_테스트  
 - AI_에이전트  
 - 취약점_스캔  
 - CI_CD_통합  
 - 자동화_펜테스트  
aliases:  
 - Strix_AI  
 - AI_해커_에이전트  
 - 취약점_자동_검출  
url: https://github.com/usestrix/strix  
---
Strix는 AI 기반 보안 테스트 도구로, 실제 해커처럼 동작하는 자율 에이전트 팀을 활용해 애플리케이션의 취약점을 탐지하고 실제 PoC(Proof of Concept)로 검증합니다. 개발자 및 보안 팀을 위해 정적 분석 도구의 오탐률을 줄이면서 빠르고 정확한 보안 테스트를 제공하며, GitHub Actions 및 CI/CD 파이프라인과의 통합을 지원합니다. Docker, Python 런타임, 브라우저 자동화 등 다양한 기능을 통해 종합적인 취약점 평가를 수행합니다.  

> **핵심 기능**:  
> - 다양한 공격 시나리오 검증을 위한 에이전트 팀 협업  
> - SQL 인젝션, XSS, 권한 상승 등 주요 취약점 탐지  
> - CLI 기반 개발자 친화적 인터페이스 및 보고서  
> - 클라우드 기반 호스팅 서비스(app.strix.ai) 지원  

> **사용 사례**:  
> - 애플리케이션 보안 테스트, 자동화된 펜테스트  
> - CI/CD 파이프라인에서 취약 코드 차단  
> - 버그 바운티 연구 및 PoC 생성 자동화  

> **요구 사항**:  
> - Docker 설치 및 LLM 제공자 API 키(예: OpenAI) 필요  
> - 로컬 또는 클라우드 환경에서 실행 가능  

> **주요 통합**:  
> - GitHub 리포지토리 스캔, 웹 애플리케이션 평가  
> - CI/CD(예: GitHub Actions)와 연동해 코드 변경 시 자동 테스트  

> **보안 주의**:  
> - 테스트 권한은 반드시 소유자에게 확인 후 수행해야 함.  
> - 윤리적·법적 사용이 필수적임.  

> **커뮤니티**:  
> - [공식 문서](https://docs.strix.ai), [Discord](https://discord.gg/strix-ai) 지원.  
> - 오픈소스 프로젝트로 기여(코드, 문서, 기술) 환영.  

> **라이선스**: Apache 2.0.  
> **추천 모델**: OpenAI GPT-5, Anthropic Claude Sonnet 4.5 등.