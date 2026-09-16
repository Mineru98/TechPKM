---
Language: TypeScript
tags:
 - x509
 - certificate
 - webcrypto
 - cryptography
 - typescript
aliases:
 - @peculiar/x509
 - peculiar x509
 - X509CertificateGenerator
url: https://github.com/PeculiarVentures/x509
---
@peculiar/x509은 @peculiar/asn1-schema 기반의 TypeScript/JavaScript 라이브러리로, X.509 인증서 및 PKCS#10 인증서 요청 생성, 인증서 파싱, 인증서 체인 검증, PKCS#7 내보내기 등을 쉽게 수행할 수 있게 해준다. 브라우저와 Node.js 환경을 모두 지원하며, WebCrypto API 호환 암호 프로바이더를 교체하여 사용할 수 있다. Reflect API 폴리필(예: reflect-metadata) 설치가 필수 요구사항이다.