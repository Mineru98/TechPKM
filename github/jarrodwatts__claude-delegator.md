---
Language: Python  
tags:  
 - AI 전문가 에이전트  
 - 코드 분석  
 - 코드 보안  
 - 자동 라우팅  
 - Claude 플러그인  
aliases:  
 - Claude 전문가 위임자  
 - 코드 전문 에이전트  
 - Claude Delegator  
url: https://github.com/jarrodwatts/claude-delegator  
---  
Claude Delegator는 Claude Code용 GPT 전문가 서브에이전트 플러그인입니다. 아키텍처 설계, 보안 분석, 코드 검토 등 5가지 전문 분야에서 복잡한 작업을 자동으로 처리합니다. 사용자의 요청에 따라 적절한 전문가를 선택하고, 분석 또는 구현 모드로 작동하며, 결과를 Claude가 통합하여 제공합니다.  

주요 기능으로는 도메인 전문가 자동 할당, 이중 모드 지원(분석/구현), 합성 응답 생성 등이 포함됩니다. 간단한 작업은 Claude가 직접 처리하지만, 복잡한 문제(보안 검토, 설계 결정, 디버깅 등)에서 GPT 전문가 팀이 개입합니다. Codex CLI를 기반으로 동작하며, 설정 파일 및 프롬프트 템플릿을 통해 사용자 정의가 가능합니다.