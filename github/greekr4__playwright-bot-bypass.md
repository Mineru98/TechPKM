---
Language: JavaScript
tags:
 - Playwright
 - BotDetectionBypass
 - WebScraping
 - StealthBrowser
 - ClaudeCodeSkill
aliases:
 - playwright-bot-bypass
 - 스텔스 브라우저
 - 봇 감지 우회
url: https://github.com/greekr4/playwright-bot-bypass/blob/main/README.md
---
기존의 스텔스 도구인 rebrowser-playwright와 실제 헤드드 Chrome, undetected-chromedriver를 하나로 통합하여 에이전트가 즉시 사용할 수 있도록 패키징한 Claude Code 스킬입니다. 복잡한 설정 조합 대신 단일 임포트 팩토리(`createStealthBrowser()`)를 제공하며, 잘못된 navigator 위조를 제거하고 검증된 레시피만을 적용해 주요 봇 감지기(9/9)를 우회합니다. QA 및 접근성 테스트 등 승인된 목적의 웹 자동화 환경에서 봇 차단 없이 안정적으로 콘텐츠에 접근할 수 있도록 지원합니다.