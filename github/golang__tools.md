---
Language: Go
tags:
 - 정적분석
 - 언어서버
 - 코드분석
 - 개발도구
 - Go언어
aliases:
 - Go Tools
 - golang.org/x/tools
 - gopls
 - goimports
 - Go 정적분석 도구
url: https://github.com/golang/tools
---
이 프로젝트는 Go 프로그램의 정적 분석과 언어 서버 프로토콜(LSP)을 지원하는 다양한 도구와 패키지를 제공합니다. 주요 기능으로는 코드 포맷팅, 호출 그래프 생성, 제어 흐름 분석, 타입 체킹 등이 있으며, VSCode 등의 편집기에서 IDE 기능을 구현할 수 있도록 지원합니다. Go 개발 생태계 내에서 코드 분석 및 리팩토링 도구로 널리 활용됩니다. 핵심 구성 요소로는 `gopls` 언어 서버와 `go/ssa` 정적 분석 프레임워크가 있습니다.