---
Language: JavaScript
tags:
 - gRPC
 - React
 - 실시간 채팅
 - Envoy 프록시
 - 프로토콜 버퍼
aliases:
 - react-grpc-chat
 - 실시간 채팅 앱
 - grpc-web 채팅
url: https://github.com/parkgeonhu/react-gRPC-chat
---
이 프로젝트는 gRPC와 React를 활용한 실시간 채팅 애플리케이션입니다. Envoy 프록시를 통해 HTTP/1.1과 HTTP/2 간 변환을 처리하며, 프로토콜 버퍼(protobuf)로 정의된 메시지 스키마를 기반으로 서버-클라이언트 간 통신을 구현했습니다. Node.js 기반 gRPC 백엔드 서버와 React 프론트엔드가 결합되어 있으며, 서버 스트리밍을 통해 실시간 메시지 전송이 가능합니다. `chat.proto` 파일에 정의된 서비스 인터페이스와 메시지 구조를 사용하여 채팅 기능을 구현하였습니다.