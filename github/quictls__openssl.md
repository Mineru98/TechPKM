---
Language: C
tags:
 - QUIC
 - TLS
 - OpenSSL
 - 암호학
 - 네트워크 프로토콜
aliases:
 - OldQuicTLS
 - quictls-fork
 - OpenSSL-QUIC
 - QUIC TLS 라이브러리
url: https://github.com/quictls/openssl
---
이 프로젝트는 QUIC 프로토콜을 지원하는 TLS 구현을 위해 OpenSSL을 포크한 것입니다. 공식 OpenSSL 배포판에 QUIC 핸드셰이크 API를 추가하여 Microsoft의 MsQuic 및 Google Chromium 등의 QUIC 구현체와 호환되도록 설계되었습니다. OpenSSL 3.1.7까지의 업데이트를 추적했으며, 현재는 퀵 TLS 기능을 제공하는 과도기적 솔루션으로 유지보수되고 있습니다. QUIC 지원이 필요하지 않은 경우 공식 OpenSSL 사용을 권장합니다. 라이브러리 버전 번호에는 'Q'를 나타내는 '81' 접두사가 추가되어 구별됩니다. 현재는 Akamai와 Microsoft가 주도하며, 커뮤니티 기여를 환영합니다.  

> **참고**: 이 저장소는 아카이브되었으며, 새로운 기능은 [quictls/quictls](https://github.com/quictls/quictls) 저장소에서 관리됩니다.