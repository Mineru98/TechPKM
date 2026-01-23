---
Language: Python
tags:
 - LLM
 - 대규모-컨텍스트-추론
 - GPU-최적화
 - 오프라인-작업
 - 멀티모달
aliases:
 - oLLM
 - 대규모-컨텍스트-LLM
 - 저비용-GPU-추론
url: https://github.com/Mega4alik/ollm
---
oLLM은 100k 컨텍스트를 지원하는 대형 언어 모델(LLM) 추론을 위한 경량 파이썬 라이브러리입니다. 허깅페이스 트랜스포머와 파이토치 기반으로 구축되었으며, 8GB VRAM의 소비자 GPU에서 gpt-oss-20B, qwen3-next-80B, Llama-3.1-8B-Instruct 등의 모델을 효율적으로 실행할 수 있습니다. SSD 오프로딩, 플래시 어텐션, 청킹된 MLP 기술을 통해 VRAM 사용량을 획기적으로 줄이며, 멀티모달(이미지/오디오) 모델도 지원합니다. 주요 사용 사례는 대규모 문서 분석, 로그 처리, 의료 기록 요약 등입니다. NVIDIA/AMD/Apple Silicon GPU와 호환됩니다.