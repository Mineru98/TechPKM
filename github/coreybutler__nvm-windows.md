---
Language: Go  
tags:  
 - Node.js 버전 관리  
 - Windows 도구  
 - 개발 환경 관리  
aliases:  
 - nvm-windows  
 - 윈도우 노드 버전 관리자  
url: https://github.com/coreybutler/nvm-windows  
---
NVM for Windows는 Windows 환경에서 여러 Node.js 버전을 관리할 수 있는 도구입니다. Microsoft, npm, Google에서 권장하는 Windows용 Node.js 버전 관리자로, 기존 Node 설치를 대체할 수 있습니다. 사용자는 `nvm install` 및 `nvm use` 명령어를 통해 원하는 Node.js 버전을 설치 및 전환할 수 있으며, 관리자 권한이 필요할 수 있습니다. 1.1.11+ 버전부터 PATH 충돌 문제 진단 기능을 제공합니다. 이 프로젝트는 Go 언어로 작성되었으며, 기존 Linux/macOS용 nvm과 다른 철학을 기반으로 합니다.  

> **참고**: 현재 이 프로젝트는 [Runtime](https://github.com/coreybutler/nvm-windows/wiki/Runtime)이라는 후속 프로젝트로 발전 중입니다.