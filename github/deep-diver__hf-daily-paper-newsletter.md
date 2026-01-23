---
Language: Go
tags:
 - GitHub Action
 - 뉴스레터 자동화
 - 머신러닝 논문 요약
 - Gemini AI
 - Google Groups 구독
aliases:
 - hf-daily-paper-newsletter
 - 매일 논문 뉴스레터
 - 허깅페이스 논문 요약
url: https://github.com/deep-diver/hf-daily-paper-newsletter
---
이 프로젝트는 허깅페이스의 🤗 Daily Papers에 게시된 논문을 자동으로 수집·요약하여 Google Groups로 뉴스레터를 발송하는 시스템입니다. GitHub Action을 활용해 매일 20:00 UTC에 실행되며, Gemini 2.5 Flash 모델로 논문 요약과 카테고리 태깅을 수행합니다. 구독자는 별도의 유지 관리 비용 없이 최신 머신러닝 논문을 매일 이메일로 받아볼 수 있습니다. 현재는 영어 논문 자동 번역 기능(한국어 우선)을 구현했습니다.