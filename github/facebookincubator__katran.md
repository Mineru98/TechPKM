---
Language: C++
tags:
 - XDP
 - BPF
 - LoadBalancing
 - Networking
 - L4
aliases:
 - 카트란
 - Katran-LB
 - XDP-LoadBalancer
 - Berkeley-Packet-Filter
url: https://github.com/facebookincubator/katran
---
카트란은 고성능 레이어 4(L4) 로드 밸런싱을 위한 C++ 라이브러리 및 BPF 프로그램입니다. XDP 인프라를 활용하여 커널 내에서 패킷 처리를 가속화하는 것이 핵심 기능이며, 특히 드라이버 모드에서 뛰어난 성능을 발휘합니다. 네트워크 토폴로지, 연결 추적, 해시 기반 서버 선택 등의 기능을 통해 확장성과 안정성을 보장합니다.

카트란은 XDP 기술을 기반으로 패킷 처리 지연을 최소화하고, NIC RX 큐 수에 따라 선형적으로 성능을 확장합니다. IPIP 캡슐화를 지원하며, RSS와 호환되는 유연한 패킷 전달 방식을 제공합니다. 주로 데이터 센터 환경에서 L7 로드 밸런서 확장용으로 설계되었습니다.