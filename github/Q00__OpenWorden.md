---
Language: Markdown
tags:
 - AI에이전트
 - 워든패턴
 - 방향성관리
 - SSOT
 - 자동화
aliases:
 - OpenWorden
 - Warden pattern
 - AI 에이전트 프로젝트 관리
url: https://github.com/Q00/OpenWorden/blob/main/README.md
---

OpenWorden은 다수의 AI 에이전트나 인간이 병렬로 작업하는 프로젝트에서 작업의 방향성을 유지하기 위한 'Warden pattern'을 패키지 형태로 제공합니다. 이 프로젝트는 에이전트가 직접 구현하는 대신, 프로젝트의 공식 정보원(SSOT)을 주기적으로 검토하여 작업의 이탈을 감지하고 증거 기반의 리뷰 노트를 남기는 감시자 역할을 수행하도록 설계되었습니다. 결과적으로 불필요한 범위 확장이나 무원칙적인 자동화 실행을 방지하고, 인간과 에이전트가 프로젝트의 본질적인 목표에 맞게 일관되게 나아갈 수 있도록 돕습니다.