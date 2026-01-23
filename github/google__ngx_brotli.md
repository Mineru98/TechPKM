---
Language: C
tags:
 - nginx 모듈
 - Brotli 압축
 - 웹 성능 최적화
 - HTTP 모듈
 - 정적/동적 압축
aliases:
 - ngx_brotli
 - nginx brotli
 - brotli nginx 모듈
url: https://github.com/google/ngx_brotli
---
ngx_brotli는 Nginx 웹 서버에서 브로틀리(Brotli) 압축을 지원하는 두 개의 모듈(필터 모듈 및 정적 모듈)을 제공하는 프로젝트입니다. 이 모듈은 동적 응답 압축과 사전 압축된 `.br` 파일 제공을 통해 웹 콘텐츠 전송 효율성을 높이는 것을 목적으로 합니다. 브로틀리 알고리즘은 우수한 압축률과 적절한 속도를 제공하며, Nginx 설정 지시어(`brotli`, `brotli_static` 등)를 통해 유연하게 구성할 수 있습니다. 주요 기능은 압축 수준, MIME 타입 필터링, 사전 압축 파일 우선 제공 등이 포함됩니다.