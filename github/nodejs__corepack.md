---
Language: JavaScript  
tags:  
 - Node.js  
 - 패키지 관리자  
 - corepack  
 - 의존성 관리  
 - CLI 도구  
aliases:  
 - Corepack  
 - Node 패키지 관리자  
 - Corepack CLI  
url: https://github.com/nodejs/corepack  
---
Corepack는 Node.js 프로젝트에 패키지 관리자 사용 환경을 제공하는 도구로, Yarn, npm, pnpm을 별도로 설치하지 않고도 사용할 수 있게 합니다. 프로젝트 설정에 따라 자동으로 호환되는 패키지 관리자 버전을 다운로드하고 관리하며, `package.json`의 `packageManager` 필드를 통해 명시적 버전 및 해시 기반 무결성 검증을 지원합니다. 오프라인 워크플로, 시스템 전체 업데이트, 커스텀 URL 지원 등 유연한 기능을 제공합니다.