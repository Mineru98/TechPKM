---
Language: Python
tags:
 - LLM
 - Ollama
 - 플러그인
 - 자연어처리
 - AI
aliases:
 - llm-ollama
 - ollama-llm
 - llm-ollama-plugin
 - ollama-integration
url: https://github.com/taketwo/llm-ollama
---
이 프로젝트는 Ollama 서버에서 실행되는 모델에 접근할 수 있도록 하는 LLM 플러그인입니다. 로컬 또는 원격 Ollama 서버와 통합되어 다양한 모델(텍스트 생성, 멀티모달, 임베딩 등)을 프롬프트, 채팅, 도구 활용에 사용할 수 있습니다. 설치 후 `llm` CLI와 Python 비동기 API를 통해 모델을 간편하게 호출할 수 있으며, 모델 별칭, 옵션 설정, 인증 등 고급 기능도 지원합니다.  

주요 기능으로는 이미지 첨부 지원, 웹 검색 도구 통합, 구조화된 출력(JSON 스키마), 컨텍스트 길이 제어, 비동기 모델 사용 등이 포함됩니다. Ollama의 기본 포트(`localhost:11434`) 외에 원격 서버 연결 및 인증(베어러 토큰, 서비스 토큰 등)도 가능합니다.