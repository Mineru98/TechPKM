---
Language: Python  
tags:  
 - 무한 컨텍스트 트랜스포머  
 - 트랜스포머 최적화  
 - 대규모 시퀀스 학습  
 - HuggingFace Transformers  
 - Llama3/Gemma 지원  
aliases:  
 - InfiniTransformer  
 - Infini-Attention  
 - 무한 어텐션 구현  
 - 트랜스포머 메모리 최적화  
url: https://github.com/Beomi/InfiniTransformer  
---  
InfiniTransformer는 "Leave No Context Behind" 논문에서 제안된 무한 컨텍스트 트랜스포머를 PyTorch/🤗Transformers로 비공식 구현한 프로젝트입니다. Llama3 및 Gemma 모델 아키텍처를 지원하며, 두 가지 유형의 Infini-Attention 구현 방식을 제공합니다. Type I은 모델/트레이너 수준의 깊은 수정으로 메모리 사용량을 크게 줄여 초대규모 시퀀스(1M 토큰 이상) 학습이 가능하며, Type II는 어텐션 레이어만 수정하여 HuggingFace 생태계와 호환성을 유지합니다. 주요 적용 사례로는 문서 처리, 장문 요약, 장기 의존성 학습이 필요한 태스크가 있습니다.