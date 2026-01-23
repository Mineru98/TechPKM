---
Language: Go
tags:
 - 컨테이너 암호화
 - OCI 이미지
 - containerd 확장
 - 암호화 라이브러리
 - CLI 도구
aliases:
 - imgcrypt
 - containerd-암호화
 - 이미지 암호화
url: https://github.com/containerd/imgcrypt
---
`imgcrypt`는 컨테이너 이미지 암호화 기능을 제공하는 containerd의 서브프로젝트로, 암호화된 OCI 이미지의 디코딩/암호화를 지원하는 라이브러리 및 CLI 도구(ctd-decoder, ctr-enc)를 포함합니다. `ocicrypt` 라이브러리와 연동하여 이미지 레이어의 암호화 작업을 수행하며, Kubernetes와 연동 시 CRI 디코더로 활용 가능합니다. 이 프로젝트는 Apache 2.0 라이선스로 공개되어 있으며, containerd 1.3 이상 버전에서 사용 가능합니다.