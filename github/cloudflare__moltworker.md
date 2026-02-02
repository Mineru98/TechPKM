---
Language: TypeScript
tags:
 - CloudflareWorkers
 - OpenClaw
 - AIAssistant
 - DevOps
 - SelfHosted
aliases:
 - Moltworker
url: https://github.com/cloudflare/moltworker
---
이 프로젝트는 개인용 AI 어시스턴트인 OpenClaw(Moltbot)를 Cloudflare Workers의 샌드박스 컨테이너 기술을 사용하여 실행하기 위한 PoC(개념 증명) 배포판입니다. Anthropic의 Claude API를 통합하여 웹 기반 제어 UI, 다중 채널(텔레그램, 디스코드, 슬랙) 지원, 장치 페어링, Cloudflare Access를 통한 관리자 페이지 보안 기능을 제공합니다. 사용자가 별도의 서버 인프라를 구축하지 않고도 Cloudflare 플랫폼 내에서 항상 켜진(on-demand) AI 환경을 구축하고 R2 저장소를 통해 대화 기록을 유지할 수 있도록 지원합니다.