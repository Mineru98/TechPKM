---
Language: TypeScript
tags:
 - 터미널
 - 브라우저
 - electron
 - rust
 - 코딩에이전트
aliases:
 - terminal-browser
 - 터미널 브라우저
 - zenbu terminal-browser
url: https://github.com/zenbu-labs/terminal-browser
---
terminal-browser는 kitty 그래픽 프로토콜과 Electron의 오프스크린 렌더링을 활용해 Chromium 기반의 실제 브라우저를 터미널 안에서 구동하는 프로젝트다. 코딩 에이전트와 같은 터미널 탭에서 웹을 사용하거나, SSH 환경에서 원격 서버의 웹사이트를 로컬에서 미리 볼 수 있으며, `--app-mode`를 통해 브라우저 기술로 터미널 앱을 만들 수도 있다. UI는 Rust 기반 그래픽 엔진과 커스텀 React 렌더러로 구현되었다.