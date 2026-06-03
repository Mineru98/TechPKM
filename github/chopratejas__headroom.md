---
Language: Python
tags:
 - AI-Agent
 - Context-Compression
 - LLM
 - MCP
 - Token-Optimization
aliases:
 - Headroom
 - 헤드룸
 - AI 에이전트 컨텍스트 압축
url: https://github.com/chopratejas/headroom/blob/main/README.md
---
AI 에이전트가 처리하는 툴 출력, 로그, RAG 청크, 대화 기록 등의 컨텍스트를 LLM 전송 전에 60~95% 압축하여 토큰 사용량을 대폭 절감해주는 컨텍스트 압축 레이어입니다. 라이브러리, 프록시, 에이전트 래핑, MCP 서버 등 다양한 방식으로 통합할 수 있으며, 로컬에서 실행되고 원본 데이터를 필요 시 복원할 수 있는 가역 압축(CCR)을 지원합니다. Claude, Codex, Cursor 등 다양한 에이전트 간의 메모리 공유와 실패 세션 학습 기능도 제공합니다.