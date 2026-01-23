---
Language: Go  
tags:  
 - ReverseProxy  
 - LoadBalancer  
 - 마이크로서비스  
 - Kubernetes  
 - Docker  
aliases:  
 - Traefik  
 - 트래픽  
 - 리버스프록시  
url: https://github.com/traefik/traefik  
---  
Traefik는 현대적인 HTTP 리버스 프록시 및 로드 밸런서로, 마이크로서비스 배포를 쉽게 할 수 있도록 설계되었습니다. Docker, Kubernetes, Consul 등과 같은 기존 인프라 구성 요소와 통합되어 자동으로 동적 구성을 수행하며, 서비스 레지스트리/오케스트레이터 API를 모니터링하여 실시간으로 라우트를 생성합니다.  

주요 기능으로는 Let's Encrypt를 통한 HTTPS 지원, 다양한 로드 밸런싱 알고리즘, 실시간 설정 업데이트, 웹 UI 및 메트릭스 제공, WebSocket/HTTP/2/gRPC 호환성 등이 포함됩니다. 단일 바이너리 또는 공식 Docker 이미지로 제공되며, 커뮤니티 및 상용 지원을 모두 이용할 수 있습니다.