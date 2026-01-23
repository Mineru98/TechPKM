---
Language: Python  
tags:  
 - LLM 추론  
 - 대규모 컨텍스트 처리  
 - GPU 최적화  
 - 오프라인 워크로드  
 - 멀티모달 지원  
aliases:  
 - oLLM  
 - 대규모 컨텍스트 LLM 추론  
 - 저비용 GPU LLM 실행  
 - 오프라인 LLM 처리  
url: https://github.com/Mega4alik/ollm  
---
oLLM은 Huggingface Transformers와 PyTorch 기반의 경량 Python 라이브러리로, 8GB VRAM GPU에서 100k 컨텍스트를 사용하는 대형 LLM 추론을 가능하게 합니다. Qwen3-Next-80B, Llama-3.1-8B-Instruct 등 대형 모델도 SSD 오프로딩과 FP16/BF16 정밀도만으로 실행하며, 이미지/텍스트/오디오 멀티모달 처리를 지원합니다. 계약 분석, 의료 기록 요약, 대규모 로그 처리 등 오프라인 워크로드에 최적화되어 있습니다.  

핵심 기능:  
- 모델 가중치 및 KV 캐시 SSD 오프로딩  
- FlashAttention-2 기반 메모리 최적화  
- AMD/애플 실리콘 포함한 다양한 GPU 지원  
- PEFT 어댑터를 통한 모델 커스터마이징