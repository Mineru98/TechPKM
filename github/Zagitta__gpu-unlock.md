---
Language: C
tags:
 - NVIDIA
 - GPU
 - Linux커널모듈
 - 텐서코어
 - AI가속
aliases:
 - gpu_unlock
 - gpu-unlock
 - 지피유언락
url: https://github.com/Zagitta/gpu-unlock
---
gpu-unlock는 NVIDIA GeForce RTX 20/30/40 시리즈 카드에서 FP16/BF16/TF32 텐서 코어가 절반 속도로 제한되어 있는 제한을 부팅 시점에 해제하는 리눅스 커널 모듈이다. 패치된 드라이버나 VBIOS 플래싱 없이 정식 NVIDIA 드라이버가 로드되기 전에 언락을 수행하여 최대 2배의 텐서 처리량과 LLM 프리필러, 파인튜닝, 이미지 생성 등에서 25~55%의 실측 성능 향상을 제공한다.