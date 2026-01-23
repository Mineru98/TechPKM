---
Language: C++
tags:
 - 분산파일시스템
 - 고성능스토리지
 - AI학습인프라
 - RDMAr
 - FoundationDB
aliases:
 - 3FS
 - Fire-Flyer File System
 - 3FS-메타데이터
url: https://github.com/deepseek-ai/3FS
---
3FS(Fire-Flyer File System)는 AI 학습 및 추론 워크로드를 위한 고성능 분산 파일 시스템입니다. 현대적인 SSD와 RDMA 네트워크를 활용하여 수천 개의 SSD와 수백 개의 스토리지 노드의 대역폭을 결합하며, 강력한 일관성을 제공하는 CRAQ(Chain Replication with Apportioned Queries)와 친숙한 파일 인터페이스를 특징으로 합니다. 데이터 준비, 체크포인팅, 추론용 KV캐시 등 다양한 AI 워크플로우를 지원하며, 테라바이트급 처리량과 빠른 정렬 성능을 제공합니다.  

핵심 기술 스택은 C++로 구현되었으며 FoundationDB를 메타데이터 저장소로 활용합니다. 180개 노드 클러스터에서 6.6TiB/s의 처리량을 달성한 사례가 있으며, KV캐시를 통한 DRAM 대체 솔루션도 제공합니다.