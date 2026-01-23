---
Language: Python/C++  
tags:  
 - 분산추론  
 - LLM  
 - 텐서병렬  
 - 홈클러스터  
 - 크로스플랫폼  
aliases:  
 - 분산라마  
 - DistributedLlama  
 - 홈디바이스클러스터  
 - LLM분산추론  
url: https://github.com/b4rtaz/distributed-llama  
---
분산 라마는 가정용 장치들을 이더넷 네트워크로 연결해 강력한 클러스터를 구성하고 LLM 추론을 가속화하는 프로젝트입니다. 텐서 병렬화와 고속 동기화를 통해 더 많은 장치를 사용할수록 성능이 향상되며, 리눅스/macOS/윈도우와 ARM/x86_64 AVX2 CPU 아키텍처를 모두 지원합니다. Qwen 3, Llama 3 시리즈 등 다양한 양자화 모델을 지원하며, 단일 명령어로 루트 노드를 설정할 수 있습니다.  

### 핵심 기능  
1. **분산 추론**: 2^n 노드 구성으로 RAM 사용량 분산 및 병렬 처리  
2. **크로스플랫폼**: Windows/Linux/macOS 및 Raspberry Pi 지원  
3. **모델 호환성**: Q40/Q80 양자화 모델 및 0.6B~405B 다양한 규모의 LLM 지원  
4. **명령어 기반 실행**: `dllama inference/chat/worker/api` 명령어로 간편한 작업 실행  

### 제한 사항  
- 노드 수는 모델의 KV 헤드 수 이하로 제한  
- 지원되는 양자화 유형(q40/q80, f32)에만 호환  

### 기술 스택  
- Python/C++ 혼합 구현  
- Vulkan 지원(실험적)  
- 멀티쓰레드 CPU 최적화