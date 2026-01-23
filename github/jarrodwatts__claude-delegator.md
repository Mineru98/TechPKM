---
Language: JavaScript
tags:
 - GPT 전문가 에이전트
 - 코드 분석 및 구현
 - 보안 및 아키텍처 검토
 - Claude 플러그인
 - MCP 통합
aliases:
 - Claude Delegator
 - Claude 전문가 위임자
 - GPT 전문가 팀
url: https://github.com/jarrodwatts/claude-delegator
---
Claude Delegator는 Claude Code 인스턴스에 GPT 기반 전문가 에이전트 팀을 제공하는 플러그인입니다. 아키텍처 설계, 보안 분석, 코드 리뷰, 계획 검증 등 5가지 전문 분야의 GPT 전문가들이 복잡한 작업을 자동으로 처리하도록 설계되었습니다. 사용자의 요청에 따라 전문가가 분석 모드(읽기 전용) 또는 구현 모드(코드 수정)로 작동하며, Claude가 전문가 출력을 종합하여 응답합니다. Codex CLI와 MCP(Meta Cognitive Protocol)를 기반으로 동작하며, 커스터마이징 가능한 전문가 프롬프트와 자동 라우팅 기능을 제공합니다.  

> 핵심 기능:  
> - 5명의 도메인 전문가(에드바이스/구현 이중 모드)  
> - 요청 유형 기반 자동 전문가 라우팅  
> - Claude의 합성 응답을 통한 자연스러운 결과 전달  
> - 보안, 아키텍처, 코드 품질 검증 지원