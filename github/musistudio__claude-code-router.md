---
Language: JavaScript  
tags:  
 - 모델 라우팅  
 - AI 개발 도구  
 - 멀티 프로바이더 지원  
aliases:  
 - Claude 코드 라우터  
 - ccr  
 - AI 모델 분산 처리  
url: https://github.com/musistudio/claude-code-router  
---  
Claude Code Router는 Claude Code 요청을 다양한 모델에 유연하게 라우팅하고 커스터마이징할 수 있는 강력한 도구입니다. OpenRouter, DeepSeek, Ollama 등 다양한 모델 프로바이더를 지원하며, 요청/응답 변환, 동적 모델 전환, CLI 관리, GitHub Actions 통합 등의 기능을 제공합니다. 비인터랙티브 모드, 사용자 정의 라우터 스크립트, 프리셋 관리 등을 통해 개발 환경을 최적화할 수 있습니다.  

핵심 기능:  
- **모델 라우팅**: 배경 작업, 추론, 장문 처리 등 시나리오별 모델 자동 선택  
- **플러그인 시스템**: 사용자 정의 변환기로 확장 가능  
- **CLI/웹 인터페이스**: 터미널 또는 브라우저에서 설정 관리  
- **프리셋 공유**: 설정 재사용 및 팀 협업 지원  
- **GitHub Actions 연동**: CI/CD 파이프라인에 통합  

비동기 처리를 위한 `NON_INTERACTIVE_MODE` 및 `API_TIMEOUT_MS` 설정으로 자동화 환경에 최적화되었습니다.