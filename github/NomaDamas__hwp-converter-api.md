---
Language: Kotlin
tags:
 - HWP 변환
 - API 서버
 - Javalin
 - hwplib
 - Docker
aliases:
 - HWP API 컨버터
 - HWP 텍스트 변환기
 - hwplib 기반 서버
url: https://github.com/vkehfdl1/hwp-converter-api
---
본 프로젝트는 HWP 파일을 텍스트 형식으로 변환하는 RESTful API 서버입니다. hwplib 라이브러리를 기반으로 Javalin 프레임워크와 Kotlin 언어로 개발되었으며, Docker를 통해 쉽게 배포할 수 있습니다. 사용자는 API를 통해 표 포함 전체 텍스트 또는 본문만 선택적으로 추출할 수 있으며, 현재 HWP 파일 형식만 지원하고 있습니다.  

표 처리 시 원본 레이아웃을 완벽히 유지하지 못하는 한계가 있으며, hwpx 파일은 별도의 변환 과정이 필요합니다.