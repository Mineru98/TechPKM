---
Language: TypeScript  
tags:  
 - n8n  
 - MCP  
 - AI_Agent  
 - 워크플로우_자동화  
 - TypeScript  
aliases:  
 - n8n_워크플로우_빌더  
 - MCP_서버  
 - AI_워크플로우_관리  
url: https://github.com/makafeli/n8n-workflow-builder  
---  
n8n 워크플로우 빌더 MCP 서버는 AI 어시스턴트(클로드 데스크톱, ChatGPT 등)와 n8n 자동화 플랫폼을 연결하는 모델 컨텍스트 프로토콜(MCP) 서버입니다. AI 도구를 직접 n8n에 연결하여 자연어 명령으로 워크플로우 생성, 실행, 관리를 가능하게 하며, n8n의 공식 API와 적절한 인증을 사용해 보안성을 확보했습니다. Node.js v18 이상과 n8n 인스턴스가 필요하며, Smithery.ai 호스팅 버전 또는 NPX를 통해 로컬 실행이 가능합니다.  

이 프로젝트는 TypeScript로 개발되었으며, 워크플로우 CRUD(생성/읽기/업데이트/삭제), 실행 관리, 태그 관리, 보안 감사 보고서 생성 등 15가지 도구를 제공합니다. AI 어시스턴트는 자연어 명령으로 워크플로우를 생성하거나 기존 워크플로우를 수정하고 실행할 수 있으며, Zapier, Make.com, n8n 웹 UI와 비교해 AI 기반 자동화 및 자연어 관리 기능을 강점으로 합니다.