---
Language: JavaScript
tags:
 - UI정렬
 - 에이전트스킬
 - 디자인시스템
 - Playwright
 - 자동화
aliases:
 - gridlines
 - 정렬 패스
 - alignment pass
url: https://github.com/pritamux/gridlines
---
gridlines는 UI 정렬 검토(align­ment pass)를 수행하는 에이전트 스킬입니다. 인터페이스에 수직 가이드 라인을 그려 사이드바, 툴바, 패널, 메뉴, 테이블의 요소들이 정렬 기준에서 벗어난 항목을 찾아내고, 패딩을 수정해 공통된 모서리를 공유하도록 정렬합니다. headless Chromium과 Playwright를 활용해 측정 및 JSON 리포트를 생성하며, Claude Code 등의 에이전트에서 바로 호출해 사용할 수 있습니다.