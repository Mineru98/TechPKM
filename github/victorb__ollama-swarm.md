---
Language: Shell Script
tags:
 - swarm-fork
 - ollama-integration
 - qwen2.5
 - local-ai
 - environment-configuration
aliases:
 - swarm-ollama-fork
 - ollama-환경변수
 - 로컬AI-설정
 - swarm-Qwen2.5
url: https://github.com/openai/swarm
---
이 프로젝트는 OpenAI의 Swarm을 포크한 저장소로, Ollama와의 연동을 위해 로컬 AI 환경을 지원하는 환경 변수를 추가했습니다. Ollama를 기본 엔드포인트로 사용하도록 기본 구성이 변경되었으며, 로컬에서 실행 중인 Qwen2.5 72B 모델을 기본 모델로 설정합니다. 이 저장소는 로컬 AI 인프라를 활용하는 사용자들에게 최적화된 설정을 제공합니다. 주요 변경 사항은 OPENAI_ENDPOINT와 SWARM_DEFAULT_MODEL 환경 변수 구성입니다.