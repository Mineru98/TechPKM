---
Language: Python
tags:
 - Claude-Code
 - GPT-5.5-Pro
 - CDP
 - Code-Review
 - Agent-Council
aliases:
 - insane-review
 - GPT-5.5 Pro Web Bridge
 - ChatGPT CDP Plugin
url: https://github.com/fivetaku/insane-review/blob/main/README.md
---
Claude Code 플러그인으로, API가 존재하지 않는 GPT-5.5 Pro를 ChatGPT 웹 세션에 CDP로 연결하여 프로그래밍 방식으로 코드 리뷰를 수행합니다. Claude가 관련 코드를 자동 선정하여 repomix로 패킹한 뒤 Pro에 전송하고, 응답을 파일로 저장하여 별도의 API 비용 없이 구독만으로 활용할 수 있도록 설계되었습니다. 실패 시 안전하게 중단되는 fail-closed 구조와 다른 에이전트와 협업할 수 있는 council 모드를 주요 특징으로 제공합니다.