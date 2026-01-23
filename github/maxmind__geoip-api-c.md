---
Language: C
tags:
 - GeoIP
 - IP geolocation
 - Legacy database
 - C library
 - MaxMind
aliases:
 - GeoIP Legacy C 라이브러리
 - GeoIP API C
- GeoIP 레거시
url: https://github.com/maxmind/geoip-api-c
---
GeoIP Legacy C 라이브러리는 IP 주소의 지리적 및 네트워크 정보를 조회하는 데 사용되는 C 언어 라이브러리입니다. 2022년 5월 이후 레거시 데이터베이스 지원이 종료됨에 따라, 보안 및 버그 수정만 제공되며 GeoIP2 데이터베이스로의 전환이 권장됩니다. 이 라이브러리는 GeoIP_STANDARD, GEOIP_MEMORY_CACHE 등 다양한 메모리 캐싱 옵션을 지원하며, IP 기반 위치 추적에 활용되지만 정확도에 한계가 있습니다. 우분투 PPA 또는 소스에서 빌드하여 설치할 수 있으며, 스레드 안전성 및 플랫폼별 빌드 문제 해결을 위한 가이드도 포함되어 있습니다.