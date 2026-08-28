---
Language: TypeScript
tags:
 - ACP
 - GLM
 - AI-Agent
 - ZhipuAI
 - IDE-Tool
aliases:
 - glm-acp-agent
 - GLM ACP Agent
 - Z.AI ACP Agent
url: https://github.com/stefandevo/glm-acp-agent
---
glm-acp-agent은 Z.AI / Zhipu AI의 GLM 모델 계열(GLM-5.3, GLM-5.3 Flash 등)을 추론 엔진으로 사용하는 Agent Client Protocol(ACP) 에이전트입니다. TypeScript로 작성되어 stdio를 통해 ACP 호환 IDE(Zed 등)와 연결되며, 실시간 스트리밍, 도구 호출(파일 시스템, 터미널, 웹), 이미지 분석, 세션 퍼시스턴스 등의 기능을 제공합니다. Z.AI GLM Coding Plan 전용으로 설계되었으며, 권한 모드 설정, 사고(thinking) 모드 노출, 세션별 모델 전환 등 완전한 ACP 프로토콜 준수를 지원합니다.