---
Language: C
tags:
 - Nginx 모듈
 - Zstandard 압축
 - 웹 서버
 - 성능 최적화
aliases:
 - zstd-nginx
 - Nginx Zstd 모듈
url: https://github.com/tokers/zstd-nginx-module
---
zstd-nginx-module은 Nginx의 응답 데이터 전송 크기를 줄이기 위해 Zstandard 압축 알고리즘을 구현하는 모듈입니다. 이 프로젝트는 실시간 압축 필터링(`ngx_http_zstd_filter_module`)과 사전 압축 정적 파일 전송(`ngx_http_zstd_static_module`) 기능을 제공하며, MIME 타입 필터링과 압축 수준 조정 등 세부적인 설정이 가능합니다. 현재 실험적 단계로, 문제 발생 시 이슈 제보나 풀 리퀘스트가 권장됩니다. BSD 2-Clause 라이선스로 배포됩니다.