---
Language: Rust/Python  
tags:  
 - 대규모언어모델  
 - 추론엔진  
 - 텍스트생성  
 - 최적화  
 - 분산트레이싱  
aliases:  
 - TGI  
 - Text Generation Inference  
 - 허깅페이스추론  
 - LLM추론  
url: https://github.com/huggingface/text-generation-inference  
---
Text Generation Inference는 대규모언어모델(LLM)을 배포하고 서빙하기 위한 툴킷입니다. 허깅페이스에서 실제 서비스 중인 이 프로젝트는 Rust, Python, gRPC 서버 기반으로 구축되었으며, Llama, Falcon 등 다양한 오픈소스 모델에 대한 고성능 텍스트 생성을 지원합니다. Tensor 병렬 처리, 연속 배치 처리, OpenTelemetry 기반 분산 트레이싱, Prometheus 메트릭스 등 프로덕션급 기능을 포함하며, NVIDIA/AMD GPU 및 다양한 하드웨어 플랫폼을 지원합니다. 현재 유지보수 모드로 운영되며, 향후에는 vLLM, SGLang 등 후속 엔진 사용을 권장합니다.