---
Language: Python
tags:
 - vLLM
 - LLM-배포
 - DGX-Spark
 - 양자화
 - 추론-최적화
aliases:
 - GLM-5.3-Flash NVFP4
 - DFlash2
 - GLM 5.3 Flash DGX Spark
url: https://github.com/tonyd2wild/GLM-5.3-Flash-NVFP4-DFlash2-2x-DGX-Spark
---
GLM-5.3-Flash(320B/18B 활성 MoE) 모델을 NVFP4 양자화, fp8 KV 캐시, DFlash2 스페큘러티브 디코딩과 함께 2대의 NVIDIA DGX Spark(GB10) 노드에서 텐서 병렬 2로 vLLM 기반 OpenAI 호환 서빙하는 배포 가이드입니다. SM121 실리콘에서 발생하는 7개의 day-0 버그를 패치한 Docker 이미지와 262K 토큰 컨텍스트, 46.9 tok/s의 디코딩 성능을 제공하며, 토큰 손상 문제가 없는 RedHatAI compressed-tensors 체크포인트를 기본값으로 권장합니다. 배포 보고서, 벤치마크, 크래시 포렌식 등 상세 문서를 통해 새로운 하드웨어에서 day-0 모델을 띄우기 위한 디버깅 키트도 함께 제공합니다.