---
Language: C
tags:
 - GeoIP
 - IP-지리적위치
 - 레거시-라이브러리
 - C-라이브러리
 - MaxMind
aliases:
 - GeoIP 레거시 C 라이브러리
 - GeoIP Legacy C
 - MaxMind GeoIP 레거시
 - IP 지리적 위치 라이브러리
url: https://github.com/maxmind/geoip-api-c
---
GeoIP 레거시 C 라이브러리는 IP 주소의 지리적 및 네트워크 정보를 조회하는 도구입니다. 2022년 5월 EOL(Eol of Life) 선언으로 보안 업데이트를 제외한 지원이 중단되었으며, 공식적으로는 GeoIP2 데이터베이스와 libmaxminddb 라이브러리 사용을 권장합니다. 레거시 GeoIP 데이터베이스를 활용하는 이 라이브러리는 상업용으로 제공되며, 설치 방법은 PPA, 소스 빌드(Unix/Linux, Windows) 등 다양한 옵션을 지원합니다. 스레딩 환경에서는 메모리 캐시 모드 사용 시 주의가 필요하며, UTF-8 인코딩 지원 및 다양한 캐시 옵션(GEOIP_MEMORY_CACHE, GEOIP_INDEX_CACHE 등)을 제공합니다.