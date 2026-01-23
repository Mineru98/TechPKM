---
Language: TypeScript
tags:
 - MCP
 - 문제 해결
 - 도구 추천
 - 순차적 사고
 - LLM 통합
aliases:
 - mcp-sequentialthinking-tools
 - MCP 순차적 사고 서버
 - 도구 추천 시스템
 - 문제 해결 플로우 관리
url: https://github.com/modelcontextprotocol/servers/blob/main/src/sequentialthinking/index.ts
---
이 프로젝트는 복잡한 문제를 단계별로 분해하고 각 단계에 적합한 MCP 도구를 추천받는 순차적 사고 서버입니다. LLM 기반 도구 추천, 신뢰도 점수, 실행 우선순위, 대안 도구 제시 등의 기능을 통해 체계적인 문제 해결 프로세스를 지원합니다. 사용자는 단계별 예상 결과 추적, 진행 상황 모니터링, 분기 관리 등의 기능을 활용할 수 있습니다.

## 핵심 기능
- 동적 순차적 사고 프로세스
- 각 단계별 도구 추천 및 신뢰도 평가
- 분기 생성 및 이전 사고 수정 기능
- 구성 가능한 메모리 관리 시스템
- 다양한 환경(Cline, WSL 등)의 MCP 클라이언트와의 호환성

## 구성 옵션
- `MAX_HISTORY_SIZE` 환경 변수로 최대 사고 저장 개수 설정 가능(기본값: 1000)

## 기술적 특징
- MCP(Model Context Protocol) 표준 준수
- 기존 MCP 순차적 사고 서버 확장/개선 버전
- LLM 분석을 통한 지능형 도구 매핑 시스템 구현

이 도구는 Svelte 5의 유니버설 리액티비티 연구와 같은 기술 문제 해결부터 복잡한 프로젝트 계획 수립까지 다양한 시나리오에 적용 가능합니다.