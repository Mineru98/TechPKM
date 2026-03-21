---
Language: TypeScript
tags:
 - Node.js
 - Pseudo-terminal
 - Windows Conpty
 - Terminal Emulator
 - Process Fork
aliases:
 - node-pty
 - forkpty
 - VSCode Terminal
url: https://github.com/microsoft/node-pty
---
Node.js용 `forkpty(3)` 바인딩 라이브러리로, Linux, macOS, Windows 환경에서 의사 터미널(Pseudo-terminal) 파일 디스크립터를 사용하여 프로세스를 포크하고 생성된 터미널 객체를 통해 입출력을 제어합니다. 주로 터미널 에뮬레이터 개발이나 프로그램이 터미널로 인식하도록 만들어야 하는 경우에 활용되며, Microsoft Visual Studio Code를 비롯한 다수의 터미널 구현체에서 핵심 의존성으로 사용됩니다.