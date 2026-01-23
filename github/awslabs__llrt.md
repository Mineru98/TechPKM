---
Language: Rust  
tags:  
 - Serverless  
 - AWS Lambda  
 - JavaScript 런타임  
 - Rust  
 - 성능 최적화  
aliases:  
 - LLRT  
 - Low Latency Runtime  
 - AWS LLRT  
url: https://github.com/awslabs/llrt  
---
LLRT(**L**ow **L**atency **R**un**t**ime)는 서버리스 애플리케이션의 빠른 실행과 효율적 운영을 위해 설계된 경량 JavaScript 런타임입니다. Rust로 구현되어 QuickJS 엔진을 활용하며, AWS Lambda 환경에서 기존 Node.js 대비 최대 10배 빠른 시작 속도와 2배 낮은 비용을 제공합니다. 실험적 패키지로 평가용으로만 권장되며, Node.js와의 완전한 호환성을 목표로 하지는 않습니다.  

AWS SDK v3 클라이언트 및 다양한 번들 유형을 기본 지원하며, 웹 플랫폼 API 및 비동기 처리에 부분적으로 호환됩니다. 서버리스 환경의 짧은 실행 시나리오(데이터 변환, 실시간 처리, AWS 서비스 연동 등)에 최적화되어 있습니다.