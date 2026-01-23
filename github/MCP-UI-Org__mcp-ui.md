---
Language: TypeScript
tags:
 - Model Context Protocol
 - UI SDK
 - 웹 컴포넌트
 - React
 - Remote DOM
aliases:
 - MCP-UI
 - 모델 컨텍스트 프로토콜 UI
 - mcp-ui
url: https://github.com/MCP-UI-Org/mcp-ui
---
**mcp-ui**는 Model Context Protocol(MCP)에 대화형 웹 컴포넌트를 제공하는 실험적 커뮤니티 프로젝트입니다. 서버 측에서 생성된 풍부한 UI 리소스를 클라이언트에서 안전하게 렌더링하고 호스트 환경과 상호작용할 수 있도록 지원합니다. TypeScript, Ruby, Python SDK를 통해 HTML, 외부 URL, Remote DOM 기반의 UI 스니펫을 정의하고, React 컴포넌트 또는 웹 컴포넌트로 렌더링할 수 있습니다. 호스트 간 호환성을 위한 어댑터 시스템과 다양한 보안 메커니즘이 포함되어 있습니다.  

> 핵심 기능:  
> - `@mcp-ui/server`(TypeScript): MCP 서버에서 UI 리소스 생성 유틸리티  
> - `@mcp-ui/client`(TypeScript): React 및 웹 컴포넌트로 UI 렌더링  
> - `mcp_ui_server`(Ruby), `mcp-ui-server`(Python): 각 언어 환경용 서버 SDK  
> - Remote DOM, HTML, 외부 URL 지원 및 호스트별 어댑터 통합