---
Language: Python
tags:
 - 데이터 로딩 최적화
 - GPU 활용률
 - 딥러닝 가속
 - 멀티 프로세스
 - 데이터 전처리
aliases:
 - GPU Util 99% 달성
 - 데이터 파이프라인 최적화
 - PyTorch DataLoader
url: https://github.com/myoons
---
이 프로젝트는 Cifar10 및 CelebA 데이터셋을 활용한 딥러닝 학습 시 GPU 활용률을 99%까지 끌어올리는 데이터 로딩 파이프라인 최적화 기법을 다룹니다. 주요 기법으로 멀티 프로세스 데이터 로딩(Prefetch), 작은 데이터 타입(UINT8) 사용, HDF5 Chunk 활용, 그리고 배치 재사용(Batch Echoing)을 적용하여 CPU-GPU 간 데이터 전송 병목 현상을 해결했습니다. 특히 대용량 데이터셋 처리 시 발생하는 디스크 I/O 지연 문제를 Chunk 캐시 기법으로 완화하는 방법을 제시합니다. GPU 활용률 저하 원인 파악 및 해결 프로세스를 체계적으로 정리한 것이 이 프로젝트의 핵심 교훈입니다.