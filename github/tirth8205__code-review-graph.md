---
Language: Python
tags:
 - CodeReview
 - MCP
 - Tree-sitter
 - AST
 - GraphDB
aliases:
 - Code Review Graph
 - CRG
 - 코드 리뷰 그래프
url: https://github.com/tirth8205/code-review-graph/blob/main/README.md
---
AI 코드 리뷰 도구가 전체 코드베이스를 반복적으로 읽어 토큰을 낭비하는 문제를 해결하기 위해, Tree-sitter로 코드의 구조적 그래프를 구축하고 변경 시 필수 컨텍스트만 AI에 제공하는 MCP 기반 도구입니다. 블라스트 반경 분석과 2초 이내의 증분 업데이트를 통해 리뷰에 필요한 토큰을 평균 8.2배 줄이며, Claude Code, Cursor 등 주요 AI 코딩 플랫폼과 자동 연동됩니다.