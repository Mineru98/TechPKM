---
Language: Go
tags:
 - 컨테이너 이미지 암호화
 - containerd 확장
 - OCI 표준
 - 암호화 라이브러리
 - CLI 도구
aliases:
 - imgcrypt
 - containerd-암호화
 - 컨테이너 이미지 보안
 - ocicrypt 통합
url: https://github.com/containerd/imgcrypt
---
`imgcrypt`는 containerd를 위한 암호화된 컨테이너 이미지 지원을 제공하는 서브프로젝트입니다. 이 프로젝트는 containerd에 API 확장을 추가하여 암호화된 이미지를 처리할 수 있도록 하며, `ctd-decoder` CLI 도구와 확장된 `ctr-enc` 도구를 제공합니다. OCI 표준과 호환되는 암호화된 이미지 레이어의 복호화 및 암호화 기능을 지원하며, Kubernetes와 통합 시 1.4 이상의 containerd 버전이 필요합니다. Apache 2.0 라이선스로 배포되는 오픈소스 프로젝트입니다.