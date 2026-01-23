---
Language: JavaScript
tags:
 - package-manager
 - nodejs
 - corepack
 - yarn
 - pnpm
aliases:
 - 코어팩
 - nodejs 패키지 관리자
 - corepack manager
url: https://github.com/nodejs/corepack
---
Corepack은 Node.js 프로젝트에 내장된 종속성 없는 도구로, 개발 환경에서 Yarn, npm, pnpm을 직접 설치하지 않고도 사용할 수 있게 합니다. `package.json`의 `packageManager` 필드를 기반으로 적절한 패키지 관리자를 자동으로 다운로드하고 관리하여 프로젝트의 설치 아티팩트를 보호합니다. Node.js 14.19.0 이상 버전에 기본 포함되어 있으며, 오프라인 워크플로우 및 시스템 전역 관리 기능을 지원합니다.