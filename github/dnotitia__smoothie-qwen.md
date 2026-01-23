---
Language: Python  
tags:  
 - 토큰 확률 조정  
 - 다국어 생성 향상  
 - LLM 편향 감소  
 - Qwen 모델 최적화  
 - 포스트 프로세싱  
aliases:  
 - 스무디 큐웬  
 - Smoothie-Qwen  
 - 토큰 스무딩  
 - 언어 편향 완화  
 - 다국어 균형 생성  
url: https://github.com/dnotitia/smoothie-qwen  
---
**Smoothie Qwen**은 Qwen 및 유사 모델의 토큰 확률을 조정하여 다국어 생성 균형을 개선하는 경량 조정 도구입니다. 유니코드 범위 기반 토큰 식별 및 가중치 스무딩을 통해 특정 언어의 과도한 생성을 억제하면서도 모델의 핵심 기능을 유지합니다. 실험 결과, 95% 이상의 언어 편향 감소 효과를 달성했으며, 코드 생성 등 주요 기능에는 영향을 주지 않습니다. 주요 구성 파라미터는 `min_scale`(최소 가중치 스케일링)과 `smoothness`(억제 곡선 경사도)입니다. Hugging Face를 통해 사전 조정된 모델을 배포 중입니다.