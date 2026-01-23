---
Language: Rust  
tags:  
 - 텍스트 생성  
 - 추론 엔진  
 - 대규모 언어 모델  
 - NVIDIA GPU  
 - Docker  
aliases:  
 - TGI  
 - 텍스트 생성 추론  
 - Hugging Face TGI  
url: https://github.com/huggingface/text-generation-inference  
---
텍스트 생성 추론(TGI)은 Rust, Python 및 gRPC를 기반으로 한 대규모 언어 모델 서빙 도구입니다. Hugging Face에서 Hugging Chat, 인퍼런스 API 및 엔드포인트 운영에 사용되며, Llama, Falcon, BLOOM 등 다양한 오픈 소스 모델에 대한 고성능 텍스트 생성 및 추론 기능을 제공합니다. 분산 추적, 메트릭 수집, 텐서 병렬 처리, 스트리밍 생성 및 양자화 지원을 포함한 프로덕션급 기능을 갖추고 있습니다.