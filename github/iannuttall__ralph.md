---
Language: JavaScript
tags:
 - AI-Agent
 - Autonomous-Coding
 - CLI
 - Git
 - LLM
aliases:
 - 랄프
 - Ralph Agent
 - 파일 기반 에이전트 루프
url: https://github.com/iannuttall/ralph/blob/main/README.md
---
Ralph은 파일과 Git을 메모리로 사용하는 최소한의 자율 코딩 에이전트 루프입니다. 매 반복마다 상태를 새로 읽어들이고 PRD(JSON)에 정의된 스토리를 기준으로 한 번에 하나씩 작업을 커밋합니다. 다양한 AI 에이전트 실행기를 연동할 수 있으며, 프로젝트 내 상태와 로그를 `.ralph/` 디렉터리에 체계적으로 관리합니다.