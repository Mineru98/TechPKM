---
Language: Go
tags:
 - caddy
 - brotli
 - 압축
 - 웹서버
 - 인코딩
aliases:
 - Caddy-Brotli
 - caddy-brotli
 - Brotli 인코딩
 - Caddy 압축
url: https://github.com/ueffel/caddy-brotli
---
이 프로젝트는 Caddy 웹 서버에 Brotli 압축 알고리즘을 구현하는 Go 패키지입니다. Caddy 2 이상에서 사용 가능하며, 순수 Go 기반 Brotli 라이브러리를 활용합니다. 높은 압축률 대신 성능이 저하되므로 주 압축 방식으로는 권장되지 않으며, Zstd와 gzip 조합을 대안으로 제시합니다. Caddyfile 설정에서 `br` 인코딩 지시어를 사용해 압축 수준을 지정할 수 있습니다.  

`encode` 지시어를 통해 gzip과 Brotli를 동시에 구성하거나, 압축 수준(기본값 4)을 직접 제어할 수 있습니다. 클라이언트 요청 헤더의 `Accept-Encoding` 우선순위에 따라 응답 인코딩이 결정됩니다. Caddy v2.4.0 이상에서는 정의 순서 또는 `prefer` 설정으로 인코딩 우선순위를 명시적으로 지정할 수 있습니다.