---
Language: Python  
tags:  
 - LLaMA  
 - 텍스트 분류  
 - 자연어 처리  
aliases:  
 - LLaMA 텍스트 분류  
 - llama-classification  
 - LLaMA 기반 분류  
url: https://github.com/sh0416/llama-classification  
---
LLaMA 모델을 활용한 텍스트 분류 코드베이스입니다. AG News 데이터셋 기준으로 조건부 확률 비교(direct, channel 방법)와 생성 기반(generate) 접근법을 실험하며, 교정(calibration)을 통한 정확도 향상 연구를 포함합니다. NVIDIA V100 GPU 환경에서의 실행 및 허깅페이스 데이터셋 호환성을 지원합니다.  

```markdown
# LLaMA 기반 텍스트 분류 프로젝트

## 핵심 기능
- **Direct 방법**: 조건부 확률 `p(y|x)` 비교를 통한 분류
- **Channel 방법**: 역방향 조건부 확률 `p(x|y)` 비교
- **교정 기능**: Direct 방법 성능 향상을 위한 교정 모듈
- **생성 기반 평가**: 텍스트 생성 모드에서의 분류 실험

## 기술 스택
- **모델**: Meta LLaMA (7B 파라미터 버전)
- **하드웨어**: NVIDIA V100 34G GPU
- **데이터셋**: AG News (HuggingFace 호환 가능)

## 성능 결과
| 방법 | 정확도 | 실행 시간 |
|-------|--------|-----------|
| Direct | 76.82% | 38분 40초 |
| Direct+교정 | 85.67% | 38분 40초 |
| Channel | 78.25% | 38분 37초 |
```