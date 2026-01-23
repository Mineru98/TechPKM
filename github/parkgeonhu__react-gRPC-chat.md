---
Language: JavaScript  
tags:  
 - gRPC  
 - React  
 - Docker  
 - 실시간 채팅  
 - 프로토콜 버퍼  
aliases:  
 - gRPC 채팅 앱  
 - React gRPC 채팅  
 - gRPC Web 프록시  
url: https://github.com/parkgeonhu/envoy  
---
이 프로젝트는 gRPC와 React를 활용한 실시간 채팅 애플리케이션이다. 프록시 서버(Envoy)를 통해 HTTP1 요청을 HTTP2로 변환하여 gRPC 백엔드와 통신하며, 프로토콜 버퍼를 사용해 데이터를 직렬화한다. React 프론트엔드와 Node.js 기반 gRPC 서버를 Docker로 배포할 수 있는 구조를 제공한다.  

```protobuf
// 핵심 기능: 서버 스트리밍(join), 단방향 요청-응답(send)  
service Chat {  
    rpc join(Message) returns (stream Message)  
    rpc send(Message) returns (Message)  
}  
```