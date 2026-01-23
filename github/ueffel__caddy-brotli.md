---
Language: Go
tags:
 - Caddy
 - Brotli
 - 압축 인코더
 - 웹 성능
 - 서버 최적화
aliases:
 - Caddy-brotli
 - Caddy Brotli 인코더
 - caddy-brotli-플러그인
url: https://github.com/ueffel/caddy-brotli
---
이 프로젝트는 Caddy 2+ 서버용 Brotli 압축 인코더를 구현하는 Go 언어 기반 플러그인입니다. 순수 Go로 작성된 Brotli 구현체를 사용하며, `encode` 디렉티브를 통해 `br` 형식의 압축을 지원합니다. 고급 압축 수준(5-12)에서 성능이 저하되므로 주된 압축 알고리즘으로는 권장되지 않으며, 대신 zstd와 gzip 조합을 사용하도록 제안합니다. Caddyfile 설정에서 압축 수준과 우선순위 설정이 가능합니다.