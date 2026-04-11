---
Language: Python
tags:
 - PyTorch
 - DataLoader
 - GPU 최적화
 - HDF5
 - 딥러닝
aliases:
 - 데이터 로더 최적화
 - GPU 활용도 99%
 - Chunk Hit
url: https://github.com/myoons/Dataloader-Optimization/blob/main/README.md
---
CIFAR10 및 CelebA 데이터셋을 대상으로 딥러닝 학습 시 GPU 활용도(GPU Util)를 99%로 끌어올리기 위한 데이터 로딩 파이프라인 최적화 방법들을 다루는 프로젝트입니다. 멀티 프로세스 데이터 로딩(Prefetch), 작은 데이터 타입 사용, HDF5 Chunk를 활용한 디스크 I/O 병목 완화, 그리고 Batch Echoing 기법을 통해 병목 원인을 진단하고 해결하는 과정을 단계적으로 설명합니다.