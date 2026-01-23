---
Language: Go
tags:
 - OCI 이미지 암호화
 - 컨테이너 런타임
 - Go 라이브러리
 - PKCS#11
aliases:
 - OCIcrypt
 - ocicrypt
 - OCI 이미지 스펙 암호화
url: https://github.com/containers/ocicrypt
---
OCIcrypt 라이브러리는 OCI 이미지 스펙의 컨테이너 이미지 암호화를 구현한 Go 언어 기반의 라이브러리입니다. 이 라이브러리는 암호화 기능의 일관된 구현을 제공하며, containerd, cri-o, skopeo 등의 런타임/빌드 도구에서 사용됩니다. 주요 기능은 레이어의 암호화/복호화 인터페이스와 암호화 알고리즘의 확장성을 지원하는 블록 암호 및 키 래핑 메커니즘을 포함합니다. PKCS#11 하드웨어 보안 모듈 지원도 실험적으로 제공됩니다.