---
Language: Rust  
tags:  
 - 비밀번호 관리자  
 - Bitwarden 호환  
 - 셀프 호스팅  
 - Rust  
 - 컨테이너 배포  
aliases:  
 - Vaultwarden  
 - Bitwarden_RS  
 - 비밀번호 저장소 서버  
 - self-hosted 비밀번호 관리자  
url: https://github.com/dani-garcia/vaultwarden  
---  
Vaultwarden은 Bitwarden 클라이언트 API와 호환되는 Rust 기반 대체 서버 구현체로, 리소스 집약적인 공식 서비스 대신 셀프 호스팅에 최적화된 솔루션입니다. 개인/조직용 비밀번호 관리, 2단계 인증, 첨부 파일 지원 등 Bitwarden의 주요 기능을 제공하며, Docker/Podman 컨테이너 또는 직접 빌드를 통해 배포할 수 있습니다.  

> 주요 특징:  
> - Bitwarden 공식 클라이언트(모바일/데스크톱/브라우저)와의 완전한 호환성  
> - 개인 및 조직 기능(컬렉션, 권한 관리, 이벤트 로그 등) 지원  
> - 다양한 2단계 인증(Authenticator, FIDO2, YubiKey 등) 통합  
> - 웹 기반 관리 인터페이스와 커스텀 웹 볼트 클라이언트 포함  
> - Docker/Quay.io/ghcr.io를 통한 간편한 컨테이너 배포 가능