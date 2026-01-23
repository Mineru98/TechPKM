---
Language: Python  
tags:  
 - LLaMA 양자화  
 - GPTQ  
 - 4비트 양자화  
 - 자연어 생성  
 - 모델 최적화  
aliases:  
 - GPTQ-for-LLaMA  
 - LLaMA 양자화 도구  
 - 4비트 LLaMA  
 - GPTQ 기반 양자화  
 - 텍스트 생성 웹UI 통합  
url: https://github.com/qwopqwop200/GPTQ-for-LLaMa  
---
LLaMA 모델의 4비트 양자화를 위한 GPTQ 기반 프로젝트입니다. 원본 GPTQ 코드를 기반으로 LLaMA에 최적화된 양자화 기능을 구현하며, 메모리 효율성과 성능 개선을 목표로 합니다. 주요 기능으로 `--act-order` 및 `--true-sequential` 옵션을 통한 정확도 향상, `groupsize`를 활용한 양자화 그룹화, CUDA 커널 최적화를 통한 생성 속도 개선이 포함됩니다. RTX 3090급 GPU에서 테스트되었으며, 양자화된 모델은 원본 대비 1/4 수준의 메모리 용량으로 FP16 대비 경쟁력 있는 성능을 보입니다.  

프로젝트 요약:  
- LLaMA-7B/13B/33B/65B 모델 지원  
- 4비트 및 3비트 양자화 옵션  
- Wikitext2 기준 PPL 지표로 성능 검증  
- PyTorch 기반 CUDA 확장 구현  
- 텍스트 생성 웹UI(예: text-generation-webui)와의 통합 목적