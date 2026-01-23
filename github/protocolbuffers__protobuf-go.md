---
Language: Go  
tags:  
 - Protocol Buffers  
 - 데이터 직렬화  
 - Go 라이브러리  
 - 코드 생성기  
 - protobuf reflection  
aliases:  
 - 프로토콜 버퍼 Go 지원  
 - protobuf-go  
 - 프로토콜 버퍼 Go 구현  
url: https://github.com/protocolbuffers/protobuf-go  
---
이 프로젝트는 언어 중립적이고 플랫폼 독립적인 구조화된 데이터 직렬화 메커니즘인 Protocol Buffers(프로토콜 버퍼)의 Go 언어 구현을 제공합니다. `.proto` 파일로부터 Go 코드를 생성하는 `protoc-gen-go` 컴파일러 플러그인과 Go 런타임 라이브러리를 포함하며, 메시지 직렬화/역직렬화, JSON/텍스트 포맷 변환, 동적 메시지 생성 등의 기능을 지원합니다. 2020년 출시된 두 번째 주요 버전으로, 이전 버전(`github.com/golang/protobuf`)보다 안정적이고 확장 가능한 인터페이스를 제공합니다.  

- **코드 생성기**: `protoc` 컴파일러와 통합되어 `.proto` 스키마로부터 Go 코드 생성  
- **런타임 라이브러리**: 메시지 직렬화, 반사(reflection) 기반 동적 조작, 다양한 포맷 지원  
- **호환성**: 런타임과 생성기 버전 간 호환성 보장 (최대 1년 차이 허용)  

프로젝트는 보안, 사양 변경, 버그 수정 등의 이유로 사전 공지 없이 주요 변경이 발생할 수 있으나, 기타 변경은 6개월 전 공지됩니다.