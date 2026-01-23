---
Language: Python
tags:
 - 프록시 서버
 - 로컬 LLM
 - Anthropic API
 - Claude Code
 - Ollama
aliases:
 - Claude 라우터
 - Claude-Code 프록시
 - 로컬 LLM 연동
 - gpt-oss 라우터
 - Anthropic 호환 서버
url: https://github.com/say828/claude-router
---
Claude Router는 Claude Code를 로컬 Ollama 설치 및 오픈소스 모델과 연결하는 범용 프록시 서버입니다. Anthropic Messages API와 호환되며, 파일 CRUD 및 터미널 명령어 실행 등 Claude Code의 모든 도구를 지능적으로 변환하여 지원합니다. Python, JavaScript, Go 등 모든 언어 및 프레임워크에서 별도 설정 없이 로컬 모델을 활용한 Claude Code 기능을 사용할 수 있도록 설계되었습니다. `run.sh` 스크립트로 의존성 설치, 환경 설정, 서비스 실행을 한 번에 처리할 수 있습니다.