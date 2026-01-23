---
Language: Go  
tags:  
 - 개발 인증서  
 - 로컬 인증서  
 - TLS 개발  
 - HTTPS 테스트  
 - 암호화 도구  
aliases:  
 - mkcert  
 - 로컬 인증서 생성기  
 - 개발용 SSL 인증서  
 - mkcert 도구  
url: https://github.com/FiloSottile/mkcert  
---  
mkcert는 로컬 개발 환경에서 신뢰할 수 있는 TLS 인증서를 간편하게 생성하고 관리하기 위한 도구입니다. 실제 인증서 기관(CA)의 인증서 대신 사용할 수 있으며, 개발용 호스트(localhost, 127.0.0.1 등)에서도 안전하게 작동합니다. 시스템 신뢰 저장소에 자동으로 로컬 CA를 설치하여 신뢰 오류를 해결하며, 다양한 플랫폼에서 지원됩니다.  

> **핵심 특징**:  
> - 단일 명령어로 인증서 생성 및 시스템 등록  
> - 다양한 도메인 패턴(와일드카드, IP 주소 등) 지원  
> - Firefox, Chrome, Java 등 주요 브라우저/플랫폼 호환  
> - ECDSA, PKCS#12, S/MIME 등 고급 옵션 제공  
> - 개발 환경에서의 HTTPS 테스트 용이성  

> **주의 사항**: 생성된 `rootCA-key.pem` 파일은 보안상 공유 금지. 프로덕션 환경 사용을 권장하지 않음.