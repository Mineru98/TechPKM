---
Language: TypeScript
tags:
 - MCP
 - Mermaid
 - Diagram
 - Validation
 - Rendering
aliases:
 - MCP Mermaid Validator
 - Model Context Protocol Mermaid
 - Mermaid Diagram CLI
url: https://github.com/rtuin/mcp-mermaid-validator/blob/main/README.md---
이 프로젝트는 Model Context Protocol(MCP)을 기반으로 구축된 Mermaid 다이어그램 검증기 서버입니다. TypeScript로 작성된 이 서버는 LLM 및 MCP 호환 클라이언트가 Mermaid 다이어그램의---
Language: TypeScript
tags:
 - MCP
 - Mermaid
 - Diagram
 - Validation
 - Rendering
aliases:
 - MCP Mermaid Validator
 - Model Context Protocol Mermaid
 - Mermaid Diagram CLI
url: https://github.com/rtuin/mcp-mermaid-validator/blob/main/README.md
---
이 프로젝트는 Model Context Protocol(MCP)을 준수하는 서버로, Mermaid 다이어그램의 구문을 검증하고 이를 PNG 이미지로 렌더링하는 기능을 제공합니다. TypeScript와 Node.js child_process를 활용하여 Mermaid CLI와 상호작용하며, 검증 성공 시 Base64로 인코딩된 이미지를, 실패 시 상세한 오류 메시지를 반환하여 LLM과의 통합을 지원합니다.