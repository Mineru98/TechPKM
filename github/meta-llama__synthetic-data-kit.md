---
Language: Python  
tags:  
 - 합성데이터생성  
 - LLM파인튜닝  
 - CLI툴  
 - 데이터셋변환  
 - 메타라이믹스  
aliases:  
 - 합성데이터툴킷  
 - SyntheticDataKit  
 - Llama3파인튜닝  
 - 데이터생성CLI  
url: https://github.com/meta-llama/synthetic-data-kit  
---  
Synthetic Data Kit는 대형 언어 모델(LLM) 파인튜닝을 위한 고품질 합성 데이터셋을 생성하는 CLI 도구입니다. PDF, HTML, YouTube 등 다양한 파일 형식을 처리하여 QA 쌍, 체인 오브 사고(CoT) 데이터를 생성하고, Llama-3 계열 모델의 태스크별 추론 능력을 향상시키는 데이터셋을 구축할 수 있습니다. `ingest`, `create`, `curate`, `save-as`의 4단계 파이프라인 구조로 구성되어 있으며, vLLM 또는 외부 API를 백엔드로 사용할 수 있습니다. Lance 형식 기본 저장 및 Alpaca, ChatML 등 다양한 파인튜닝 형식 변환을 지원합니다.