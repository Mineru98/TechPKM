# Claude-Flow v3: 엔터프라이즈 AI 오케스트레이션 플랫폼

[![Star on GitHub](https://img.shields.io/github/stars/ruvnet/claude-flow?style=for-the-badge&logo=github&color=gold)](https://github.com/ruvnet/claude-flow)
[![Monthly Downloads](https://img.shields.io/npm/dm/claude-flow?style=for-the-badge&logo=npm&color=blue&label=Monthly%20Downloads)](https://www.npmjs.com/package/claude-flow)
[![Total Downloads](https://img.shields.io/npm/dt/claude-flow?style=for-the-badge&logo=npm&color=cyan&label=Total%20Downloads)](https://www.npmjs.com/package/claude-flow)
[![Latest Release](https://img.shields.io/npm/v/claude-flow/alpha?style=for-the-badge&logo=npm&color=green&label=v3.0.0-alpha)](https://www.npmjs.com/package/claude-flow)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-SDK%20Integrated-green?style=for-the-badge&logo=anthropic)](https://github.com/ruvnet/claude-flow)
[![Agentics Foundation](https://img.shields.io/badge/Agentics-Foundation-crimson?style=for-the-badge&logo=openai)](https://discord.com/invite/dfxmpwkG2D)
[![ruv.io](https://img.shields.io/badge/ruv.io-AI%20Platform-purple?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwLTQuNDggMTAtMTI+PC9wYXRoPjwvc3ZnPg==)](https://ruv.io)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative)](https://opensource.org/licenses/MIT)
[![RuVector](https://img.shields.io/npm/v/ruvector?style=for-the-badge&logo=rust&color=orange&label=RuVector)](https://www.npmjs.com/package/ruvector)
[![Agentic-Flow](https://img.shields.io/npm/v/agentic-flow?style=for-the-badge&logo=typescript&color=3178c6&label=Agentic-Flow)](https://www.npmjs.com/package/agentic-flow)

## 개요

Claude-Flow는 Claude Code를 강력한 멀티-에이전트 개발 플랫폼으로 변환하는 포괄적인 AI 에이전트 오케스트레이션 프레임워크입니다. 팀이 복잡한 소프트웨어 엔지니어링 작업에 대해 함께 작업하는 54+ 특수화된 AI 에이전트를 배포, 조정 및 최적화할 수 있도록 합니다.

### 아키텍처

```
사용자 → Claude-Flow (CLI/MCP) → 라우터 → 스웜 → 에이전트 → 메모리 → LLM 제공업체
                       ↑                          ↓
                       └──── 학습 루프 ←──────┘
```

## 설치

### 사전 요구 사항

- **Node.js 18+ 또는 Bun 1.0+ (Bun은 더 빠름)**
- **npm 9+ / pnpm / bun 패키지 관리자**

**중요**: Claude Code가 먼저 설치되어야 합니다:

```bash
# 1. Claude Code 글로벌 설치
npm install -g @anthropic-ai/claude-code

# 2. (선택 사항) 권한 검사 건너뛰기
claude --dangerously-skip-permissions
```

### 설치

```bash
# npm/npx (Node.js)
npm install claude-flow@v3alpha
npx claude-flow@v3alpha init

# Bun (더 빠름)
bun add claude-flow@v3alpha
bunx claude-flow@v3alpha init

# Claude Code 통합을 위한 MCP 서버 시작
npx claude-flow@v3alpha mcp start

# 작업 실행
npx claude-flow@v3alpha --agent coder --task "사용자 인증 구현"

# 사용 가능한 에이전트 목록
npx claude-flow@v3alpha --list
```

### 업그레이드

```bash
# 업데이트 헬퍼 및 상태선 (데이터 보존)
npx claude-flow@v3alpha init upgrade

# 업데이트 AND 누락된 스킬/에이전트/명령 추가
npx claude-flow@v3alpha init upgrade --add-missing
```

## 핵심 기능

### 🤖 54+ 특수화된 에이전트

- **핵심 개발**: coder, reviewer, tester, planner, researcher
- **V3 특화**: queen-coordinator, security-architect, memory-specialist
- **스웜 조율**: hierarchical-coordinator, mesh-coordinator, adaptive-coordinator
- **성능**: perf-analyzer, performance-benchmarker, task-orchestrator
- **GitHub & 저장소**: pr-manager, code-review-swarm, issue-tracker, release-manager
- **SPARC 방법론**: sparc-coord, specification, pseudocode, architecture
- **특수 개발**: backend-dev, mobile-dev, ml-developer, cicd-engineer

### 🐝 스웜 토폴로지

| 토폴로지 | 권장 에이전트 | 최고 성능 | 실행 시간 | 메모리/에이전트 |
|----------|----------------|----------|----------------|--------------|
| **계층적** | 6+ | 구조화된 작업, 명확한 권한 체계 | 0.20s | 256 MB |
| **메시** | 4+ | 협업 작업, 높은 중복성 | 0.15s | 192 MB |
| **링** | 3+ | 순차적 처리 파이프라인 | 0.12s | 128 MB |
| **스타** | 5+ | 중앙 집중 제어, 스포크 작업자 | 0.14s | 180 MB |
| **하이브리드 (계층적-메시)** | 7+ | 복잡한 멀티-도메인 작업 | 0.18s | 320 MB |
| **적응형** | 2+ | 동적 작업량, 자동 확장 | 가변 | 동적 |

### 🧠 학습 & 메모리 최적화

- **학습 루프**: 성공 패턴 저장 및 재사용, 라우팅 최적화
- **메모리 최적화**: 2.49x-7.47x 속도 향상, 메모리 감소
- **자동 확장**: 작업량에 따른 에이전트 생성
- **자기 치유 워크플로우**: 자동 오류 복구 및 작업 재시도
- **교차 세션 메모리**: 세션 간 패턴 저장
- **이벤트 소싱**: 완전한 감사 추적 및 재생 기능

### 🔁 스킬 시스템

확장 가능한 워크플로우 플러그인 생성:

```yaml
name: feature-pipeline
description: 엔드-투-엔드 기능 구현

stages:
  - name: research
    agent: researcher
    input: requirements
    output: analysis

  - name: design
    agent: architect
    input: analysis
    output: architecture

  - name: implement
    agent: coder
    input: architecture
    output: code

  - name: test
    agent: tester
    input: code
    output: test_results

  - name: review
    agent: reviewer
    input: [code, test_results]
    output: final_review
```

## 📦 메타데이터 문서

---
Language: TypeScript
tags:
 - AI 오케스트레이션
 - Claude Code 통합
 - 멀티 에이전트 시스템
 - 학습형 메모리
 - 엔터프라이즈 보안
aliases:
 - Claude-Flow
 - AI 에이전트 조율
 - Claude Code 플러그인
url: https://github.com/ruvnet/claude-flow
---
Claude-Flow는 Claude Code를 강력한 멀티 에이전트 개발 플랫폼으로 변환하는 포괄적인 AI 에이전트 오케스트레이션 프레임워크입니다. 팀이 복잡한 소프트웨어 엔지니어링 작업에 대해 함께 작업하는 54+ 특수화된 AI 에이전트를 배포, 조정 및 최적화할 수 있도록 합니다. 학습형 메모리, 엔터프라이즈 보안, 확장 가능한 플러그인 시스템을 통해 지속적인 학습과 고성능 AI 작업을 지원합니다.