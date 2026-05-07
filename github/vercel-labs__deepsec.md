---
Language: TypeScript
tags:
 - Security
 - Vulnerability-Scanner
 - AI-Agent
 - Vercel
 - SAST
aliases:
 - DeepSec
 - 딥섹
 - AI 취약점 스캐너
url: https://github.com/vercel-labs/deepsec/blob/main/README.md
---
자체 인프라에서 실행할 수 있는 AI 에이전트 기반 취약점 스캐너로, 대규모 레포지토리 내에 숨어있는 복잡한 보안 이슈를 탐지하는 데 목적이 있습니다. 최고 수준의 AI 모델을 활용하여 정밀한 분석을 수행하며, 대규모 코드베이스의 경우 Vercel Sandbox를 통해 병렬 분산 처리를 지원합니다. 스캔, PR 리뷰, 결과 재검증 등의 워크플로우를 제공하고 명령어 중단 후에도 이어서 작업을 수행할 수 있는 멱등성을 갖추고 있습니다.