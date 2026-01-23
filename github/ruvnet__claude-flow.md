# Claude-Flow v3: Enterprise AI Orchestration Platform

## 📌 요약

Claude-Flow v3는 Anthropic의 Claude Code를 강력한 멀티 에이전트 개발 플랫폼으로 변환하는 종합적인 AI 에이전트 오케스트레이션 프레임워크입니다. 54개 이상의 전문 AI 에이전트를 배포하고, 조정하며, 복잡한 소프트웨어 엔지니어링 작업에 최적화된 에이전트 팀을 운영할 수 있도록 지원합니다.

## 🎯 핵심 기능

### 🐝 멀티 에이전트 스웜 조정
- **54+ 전문 에이전트**: 코딩, 코드 리뷰, 테스트, 보안 감사, 문서화, DevOps 등
- **스웜 토폴로지**: 계층형, 메시, 링, 스타, 하이브리드, 적응형
- **컨센서스 프로토콜**: Raft, Byzantine, Gossip, CRDT, 가중치 기반
- **10-20배 빠른 배치 스패닝**: 최대 84.8% SWE-Bench 해결률

### 🧠 지능형 라우팅 & 학습
- **Q-러닝 기반 태스크 라우팅**: 태스크 복잡성을 분석하여 최적의 에이전트 선택
- **SONA 학습**: 0.05ms 미만의 적응 시간으로 에이전트 성능 최적화
- **패턴 학습**: 성공적인 패턴을 저장하여 미래 작업에 재사용
- **모델 라우팅**: Haiku/Sonnet/Opus의 3단계 복잡도 기반 자동 선택

### 🛡️ 엔터프라이즈 보안
- **AIDefense 보안 모듈**: 프롬프트 인젝션, 탈옥 시도, PII 노출 방지
- **입력/경로 검증**: 안전한 파일 경로 및 사용자 입력 처리
- **보안 감사**: CVE 취약점 스캔 및 보안 권고사항 제공

### 📦 확장 가능한 플러그인 시스템
- **커스텀 플러그인 개발**: MCP 도구, 후크, 워커, 보안 모듈 추가
- **IPFS 마켓플레이스**: 커뮤니티 패턴, 에이전트, 스킬 공유

### 📊 성능 최적화
- **토큰 최적화**: 30-50% 토큰 사용량 감소
- **메모리 압축**: LoRA 및 Int8 양자화로 3.92배 메모리 절약
- **에이전트 부스터**: WASM 기반 코드 변환으로 352배 빠른 처리

## 🧩 주요 구성 요소

### 📁 메모리 & 패턴 저장소
- **AgentDB**: HNSW 인덱싱으로 150x-12,500배 빠른 검색
- **ReasoningBank**: 패턴 저장 및 학습
- **EWC++**: 성공적인 패턴의 망각 방지

### 🧰 CLI 및 MCP 도구
- **26개 명령어**: 에이전트, 스웜, 메모리, MCP 서버 관리
- **175+ MCP 도구**: Claude Code와의 원활한 통합

### 🌐 클라우드 통합
- **Flow Nexus 플랫폼**: 스웜 확장, 신경망 훈련, 샌드박스 관리
- **IPFS/구글 클라우드 저장소**: 패턴 및 에이전트 구성 공유

## 🧪 테스트 프레임워크
- **런던 스쿨 TDD**: 행동 검증, 모의 객체, 고정 장치
- **Vitest 통합**: Jest보다 10배 빠른 테스트

## 📌 사용 사례

| 시나리오 | 해결 방법 | 명령어 예시 |
|----------|------------|--------------|
| 코드 리뷰 | 보안, 성능, 스타일 검사 | `/github-code-review` |
| 테스트 생성 | 단위, 통합, E2E 테스트 자동 생성 | `npx claude-flow@v3alpha --agent tester --task "테스트 작성"` |
| 보안 감사 | 취약점 탐지 및 수정 | `npx claude-flow@v3alpha --agent security-architect --task "보안 취약점 검사"` |
| 복잡한 작업 | 멀티 에이전트 병렬 처리 | `npx claude-flow@v3alpha swarm init --topology mesh` |
| 토큰 최적화 | 30-50% 토큰 절약 | `npx claude-flow@v3alpha hooks route --task "복잡한 작업"` |

## 📦 설치 및 설정

### 설치
```bash
# npm/npx (Node.js)
npm install claude-flow@v3alpha
npx claude-flow@v3alpha init

# Bun (더 빠름)
bun add claude-flow@v3alpha
bunx claude-flow@v3alpha init
```

### Claude Code MCP 통합
```bash
# Claude Code에 MCP 서버 추가
claude mcp add claude-flow -- npx claude-flow@v3alpha mcp start
```

## 📚 문서 및 지원

- **공식 문서**: [github.com/ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)
- **이슈 트래커**: [github.com/ruvnet/claude-flow/issues](https://github.com/ruvnet/claude-flow/issues)
- **전문가 구현**: [ruv.io](https://ruv.io) — 엔터프라이즈 컨설팅, 맞춤형 통합, 프로덕션 배포
- **디스코드 커뮤니티**: [Agentics Foundation](https://discord.com/invite/dfxmpwkG2D)

## 📋 라이선스

MIT - [RuvNet](https://github.com/ruvnet)