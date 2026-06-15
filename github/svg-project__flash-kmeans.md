---
Language: Python
tags:
 - K-Means
 - Triton
 - GPU
 - Clustering
 - PyTorch
aliases:
 - Flash-KMeans
 - flash_kmeans
 - IO-aware K-Means
url: https://github.com/svg-project/flash-kmeans/blob/main/README.md
---
Triton GPU 커널로 구현된 IO 인식 배치 K-Means 클러스터링 라이브러리입니다. 메모리 초과 문제를 방지하며 대규모 데이터를 효율적으로 처리하도록 설계되었으며, 단일 GPU뿐만 아니라 멀티 GPU 환경에서의 자동 확장을 지원합니다. Sparse VideoGen2 프로젝트의 공식 K-Means 구현으로 사용됩니다.