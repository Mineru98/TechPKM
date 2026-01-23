---
Language: Go  
tags:  
 - 컨테이너 이미지 관리  
 - OCI 이미지  
 - Docker 레지스트리  
 - 명령어 도구  
 - 컨테이너 보안  
aliases:  
 - skopeo  
 - 컨테이너 이미지 복사  
 - 레지스트리 인증  
url: https://github.com/containers/skopeo  
---  
`skopeo`는 컨테이너 이미지 및 레지스트리 작업을 위한 명령줄 유틸리티입니다. root 권한 없이 데몬 없이 작동하며, OCI 이미지와 Docker v2 이미지를 모두 지원합니다. 레지스트리 간 이미지 복사, 원격 이미지 검사, 이미지 삭제, 오프라인 배포를 위한 레지스트리 동기화 등의 기능을 제공합니다. 다양한 인증 방식과 컨테이너 스토리지 백엔드(예: Podman, CRI-O)와 호환됩니다.