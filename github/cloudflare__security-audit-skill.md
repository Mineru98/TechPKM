---
Language: JavaScript
tags:
 - security-audit
 - coding-agent
 - vulnerability-discovery
 - LLM-agent
 - Cloudflare
aliases:
 - security-audit-skill
 - 보안 감사 스킬
 - 취약점 발견 하네스
url: https://github.com/cloudflare/security-audit-skill/blob/main/README.md
---
security-audit은 코딩 에이전트를 보안 감사자로 변환해주는 Cloudflare의 스킬입니다. 정찰, 커버리지 기반 취약점 탐색, 후보 검증, 구조화된 출력, 독립적인 기록 검증, 중립적 보고의 6단계 구조화된 감사 워크플로를 오케스트레이션하며, Cloudflare의 취약점 발견 하네스의 단일 저장소 출발점입니다. 에이전트가 대상 코드베이스에 대해 "security audit"과 같은 요청을 받으면 자동으로 활성화되어 확인된 취약점, 검증 필요 항목, 기각된 후보를 구분하여 보고서를 생성합니다.