---
Language: Rust  
tags:  
 - AWS Lambda  
 - 서버리스 런타임  
 - JavaScript 런타임  
 - 저지연  
 - AWS SDK  
aliases:  
 - LLRT  
 - Low Latency Runtime  
 - LLRT 런타임  
url: https://github.com/awslabs/llrt  
---  
LLRT(Low Latency Runtime)는 AWS Lambda 환경에서 고성능 서버리스 애플리케이션을 위한 경량 JavaScript 런타임입니다. Rust로 구축되어 QuickJS 엔진을 기반으로 하며, 기존 런타임 대비 최대 10배 빠른 시작과 2배 낮은 비용을 제공합니다. 실험적 단계로, Node.js와의 호환성 제한 및 평가용 목적을 가집니다. AWS SDK v3 통합 및 다양한 배포 옵션(커스텀 런타임, 레이어, 컨테이너 등)을 지원합니다.