---
Language: C
tags:
 - nginx 모듈
 - Zstandard 압축
 - 웹 성능 최적화
 - 실시간 압축
 - 정적 파일 압축
aliases:
 - zstd-nginx-module
 - Zstd Nginx
 - nginx zstd 압축
 - 실시간 Zstd 압축
url: https://github.com/tokers/zstd-nginx-module
---
이 프로젝트는 Nginx 웹 서버에 Zstandard(zstd) 압축 기능을 추가하는 모듈입니다. `ngx_http_zstd_filter_module`을 통해 실시간 응답 압축을, `ngx_http_zstd_static_module`을 통해 사전 압축된 `.zst` 파일 제공 기능을 지원합니다. 압축 레벨, 최소 길이, MIME 타입 등의 세부 설정이 가능하며, 사전 압축된 정적 파일도 효율적으로 처리할 수 있습니다. 현재 실험적 단계로 분류되지만, 웹 성능 최적화를 위한 핵심 도구로 활용될 수 있습니다.