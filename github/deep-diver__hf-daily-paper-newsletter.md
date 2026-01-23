---
Language: Go
tags:
 - 뉴스레터
 - 자동화
 - 머신러닝
 - Gemini API
 - GitHub Actions
aliases:
 - HF Daily Paper Newsletter
 - Daily Papers 뉴스레터
 - 머신러닝 논문 요약
url: https://github.com/deep-diver/hf-daily-paper-newsletter
---
이 프로젝트는 Hugging Face의 Daily Papers에 게시된 머신러닝 논문들을 자동으로 수집·분석하여 구독자들에게 뉴스레터로 발송하는 시스템입니다. GitHub Actions를 통해 완전히 자동화된 워크플로우로 운영되며, Google의 Gemini 2.5 Flash 모델을 활용해 논문 요약과 카테고리 태깅을 생성합니다. 매일 오후 8시(UTC)에 전일 논문들을 대상으로 뉴스레터가 발송되며, 구독은 Google Groups를 통해 가능합니다. 현재 한국어 번역 기능이 구현되어 있습니다.