---
Language: TypeScript
tags:
 - AI-agent
 - self-hosted
 - Docker
 - browser-automation
 - multi-agent
aliases:
 - OpenGrokBot
 - 오픈그록봇
 - Grok Bot self-hosted alternative
url: https://github.com/wolfqing/OpenGrokBot
---
OpenGrokBot는 xAI의 유료 Grok Bot($120–300/월)을 대체하는 셀프호스팅 항상 켜진 AI 팀원 플랫폼입니다. 팀원(봇)마다 독립된 Docker 컨테이너 컴퓨터(헤드리드 Chromium, 셸, 파일 시스템)를 할당하고, 자격 증명은 사용자 머신의 컨테이너 안에만 보관됩니다. 초안 보류 후 승인, MEMORY.md 기반 지속 메모리, cron 루틴, 그룹 스레드 및 봇 간 핸드오프 등을 지원하며 OpenAI 호환 모델(xAI, DeepSeek, Ollama 등)을 사용할 수 있습니다.