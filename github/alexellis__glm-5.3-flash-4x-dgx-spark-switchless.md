---
Language: Python
tags:
 - LLM-serving
 - DGX-Spark
 - NCCL
 - tensor-parallelism
 - vLLM
aliases:
 - GLM-5.3-Flash TP4
 - switchless-ring
 - DFlash2
url: https://github.com/alexellis/glm-5.3-flash-4x-dgx-spark-switchless
---
NVIDIA DGX Spark 노드 4대를 스위치 없는 RoCE 링 토폴로지로 연결해 GLM-5.3-Flash(NVFP4) 모델을 하나의 텐서 병렬(TP4) 엔진으로 서빙하는 레시피 리포지토리입니다. 패치된 NCCL(switchless-nccl)과 DFlash2 스페클레이티브 디코딩을 활용해 OpenAI 호환 엔드포인트와 262K 컨텍스트 윈도우를 제공하며, 실측 벤치마크(RigMark) 결과와 운영 가이드를 함께 공개합니다. 가중치와 서빙 인자만 교체하면 다른 모델에도 적용할 수 있도록 일반화된 패브릭 구성과 런치 스크립트를 포함합니다.