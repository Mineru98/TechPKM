---
Language: Go
tags:
 - 컨테이너 이미지 암호화
 - OCI 표준
 - 이미지 암호화 라이브러리
 - containerd
 - cri-o
aliases:
 - ocicrypt
 - OCI 암호화 라이브러리
 - 컨테이너 암호화
url: https://github.com/containers/ocicrypt
---
OCIcrypt 라이브러리는 OCI 이미지 스펙 기반의 컨테이너 이미지 암호화를 구현하기 위한 라이브러리입니다. 이 라이브러리는 암호화/복호화 기능의 일관된 구현을 제공하며, containerd, cri-o, skopeo 등 다양한 런타임/빌드 툴에서 사용됩니다. 주요 기능은 레이어별 암호화/복호화 인터페이스와 확장 가능한 암호화 알고리즘 설계입니다.  

이 프로젝트는 OCI 이미지 스펙(PR #775)에 정의된 암호화 방식을 코드 수준에서 구현하며, 키 관리 및 보안 확장을 위한 인터페이스를 제공합니다. PKCS#11 지원은 현재 실험적 단계로, 추가적인 문서가 존재합니다.