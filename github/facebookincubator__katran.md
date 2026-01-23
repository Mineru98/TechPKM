---
Language: C++
tags:
 - XDP
 - LoadBalancer
 - BPF
 - 고성능네트워킹
 - L4로드밸런싱
aliases:
 - katran
 - 페이스북_로드밸런서
 - XDP_기반_로드밸런싱
url: https://github.com/facebookincubator/katran
---
Katran은 C++ 라이브러리와 BPF 프로그램으로 구현된 고성능 L4 로드밸런싱 포워딩 플랜입니다. XDP 인프라를 활용하여 커널 내에서 패킷 처리를 가속화하며, 선형 확장성과 RSS 친화적인 캡슐화를 특징으로 합니다. 주로 DSR 모드에서 동작하며, L7 로드밸런서의 확장성을 향상시키기 위해 설계되었습니다. 연결 추적을 위한 고정 크기 테이블과 수정된 Maglev 해싱 알고리즘을 사용하여 장애 복구 및 부하 분산 기능을 제공합니다.