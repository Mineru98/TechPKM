---
Language: JavaScript
tags:
 - React Native
 - CLI 도구
 - 프로젝트 템플릿
 - TypeScript
 - Expo
aliases:
 - Belt CLI
 - React Native 템플릿
 - thoughtbot 벨트
url: https://github.com/thoughtbot/belt
---
Belt는 thoughtbot에서 개발한 React Native 앱 개발을 위한 의견 기반 CLI 도구입니다. 내부적으로 검증된 도구나 관례를 기반으로 Expo, TypeScript, ESLint, Prettier 등의 기본 설정을 자동화하여 React Native 앱 개발을 간소화합니다. Tanstack Query(REST API용), React Navigation, MSW(모의 서버) 등의 핵심 기능을 포함하며, Redux Toolkit(글로벌 상태 관리) 및 Apollo Client(GraphQL) 지원은 곧 추가될 예정입니다.  

이 도구는 `create-belt-app` 명령어로 초기 프로젝트를 생성하고, `belt add [기능]` 명령어로 추가 기능을 유연하게 확장할 수 있도록 설계되었습니다. NPM, Yarn, pnpm(예실험적), Bun(예실험적)을 지원합니다.