---
Language: Bash
tags:
 - AI CLI
 - 스킬 모음
 - 슬라이드 윤문
 - 번역체 교정
 - Claude Code
aliases:
 - skill-forge
 - 스킬 포지
 - slide-ko-polish
url: https://github.com/hackertaco/skill-forge/blob/main/README.md
---
AI CLI 환경(Claude Code, OpenAI Codex, Gemini CLI)에서 동작하는 재사용 가능한 Bash 기반 스킬 모음 레포지토리입니다. 대장간(forge)처럼 직접 깎아낸 스킬들을 체계적으로 관리하고 호출할 수 있도록 설계되었습니다.

현재는 영어에서 한국어로 번역된 발표 슬라이드의 어색한 번역투를 자연스러운 한국어로 다듬는 'slide-ko-polish' 스킬이 포함되어 있습니다. 이 스킬은 정규식 스캔, HTML 구조 검증, LLM 검토 등 4단계 검증 파이프라인을 거쳐 품질을 보장하며, 설치된 LLM CLI를 자동으로 감지해 실행합니다.