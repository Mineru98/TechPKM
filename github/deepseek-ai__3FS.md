---
Language: C++
tags:
 - 분산파일시스템
 - AI학습
 - 고성능스토리지
 - RDMA
 - FoundationDB
aliases:
 - 3FS
 - Fire-Flyer File System
 - 딥시크AI 파일시스템
url: https://github.com/deepseek-ai/3fs
---
Fire-Flyer File System(3FS)은 AI 학습 및 추론 워크로드의 성능 문제를 해결하기 위해 설계된 고성능 분산 파일 시스템입니다. 현대적인 SSD와 RDMA 네트워크를 활용하여 수천 개의 SSD와 스토리지 노드의 대역폭을 통합하며, 강력한 일관성을 보장하는 CRAQ(Chain Replication with Apportioned Queries) 기술을 적용했습니다. 데이터 준비, 데이터 로더, 체크포인트, KV캐시 등 다양한 AI 워크플로우를 지원하며, FoundationDB 기반의 트랜잭션 키-값 저장소로 메타데이터를 관리합니다.  

3FS는 180개 스토리지 노드 클러스터에서 6.6TiB/s의 읽기 처리량을 달성했으며, 110.5TiB 데이터 정렬을 30분 14초에 완료하는 등 대규모 AI 인프라에 최적화된 성능을 입증했습니다. C++로 구현되었으며, 리눅스 환경에서 빌드 및 배포가 가능합니다.