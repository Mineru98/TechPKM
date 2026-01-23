---
Language: TypeScript
tags:
 - Figma 플러그인
 - n8n 자동화
 - WebSocket 통신
 - 디자인 워크플로우
 - MCP 프로토콜
aliases:
 - Figmation
 - figma-automation
 - n8n-figma-plugin
 - figma-mcp
url: https://github.com/dandacompany/figma-plugin-figmation
---
Figmation은 Figma 디자인 워크플로우를 외부 시스템과 연동하는 React 기반 Figma 플러그인입니다. n8n 워크플로우와 WebSocket 서버를 통해 Figma API 명령을 실시간 실행하며, AI 에이전트와의 통합을 통해 자연어 기반 디자인 생성을 지원합니다. 55개 이상의 Figma API 명령어를 지원하며, 멀티 채널 시스템과 자동 재연결 기능을 통해 안정적인 원격 디자인 자동화를 제공합니다.  

**핵심 기능**:  
- 55+ Figma API 명령 지원 (도형 생성, 텍스트 관리, 스타일 적용 등)  
- WebSocket 기반 실시간 n8n 통신  
- 멀티 채널 시스템 및 자동 재연결  
- 동적 페이지 로딩 및 컴포넌트 인스턴스 관리  
- 글자체 검색 및 배치 스타일 적용  

**아키텍처**:  
`외부 AI 에이전트 → n8n 워크플로우 → WebSocket 커넥터 → Figma 플러그인 → Figma 캔버스`로 이어지는 계층적 구조로, MCP(Model Context Protocol) 기반의 설계 자동화 파이프라인을 구현합니다.