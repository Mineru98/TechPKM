---
Language: Python
tags:
 - MLX
 - Sparse Retrieval
 - SPLADE
 - Apple Silicon
 - Multimodal Search
aliases:
 - SPLADE MLX
 - V-SPLADE MLX
 - SPLADE 애플 실리콘 포트
url: https://github.com/NomaDamas/SPLADE-mlx/blob/main/README.md
---
Apple Silicon의 MLX 프레임워크를 위해 네이티브로 포팅된 SPLADE 희소 검색 모델 라이브러리입니다. 텍스트 기반 SPLADE 모델뿐만 아니라 시각 문서 검색을 위한 V-SPLADE 모델도 지원하며, PyTorch MPS 대비 동일 정밀도에서 최대 2.9배 빠른 추론 속도를 제공합니다. 검색 품질 손실 없이 fp32 수준의 정확도를 유지하고, bf16 및 8비트 양자화 옵션을 통해 메모리 사용량을 최적화할 수 있습니다.