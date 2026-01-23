---
Language: Dockerfile
tags:
 - PDF 변환
 - html 변환
 - pdf2htmlEX
 - Docker 이미지
 - 문서 변환
aliases:
 - PDF2HTML 변환 도구
 - pdf2htmlex 도커
 - Docker PDF-HTML 변환기
url: https://github.com/sergiomtzlosa/docker-pdf2htmlex
---
이 프로젝트는 PDF 파일을 아름다운 HTML 형식으로 변환하는 Docker 이미지를 제공합니다. `pdf2htmlEX` 도구를 기반으로 하며, 로컬 환경에서 도커 컨테이너를 실행하거나 별칭(alias)을 설정하여 간편하게 사용할 수 있습니다. 컨테이너 볼륨 마운트 기능을 활용해 PDF 파일을 HTML로 변환하며, 오프라인 빌드와 온라인 빌드 방식을 모두 지원합니다.  

주요 특징으로는 간단한 명령어 실행(`docker run` 또는 사용자 정의 별칭), Ubuntu 기반 오프라인 이미지 생성 기능, Docker Hub를 통한 이미지 풀(pull) 지원 등이 있습니다. 변환 시 `--zoom` 옵션으로 확대/축소 조절이 가능합니다.