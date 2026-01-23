---
Language: Python  
tags:  
 - 긴_컨텍스트_처리  
 - 트랜스포머_모델  
 - 허깅페이스  
 - 효율적인_메모리_사용  
 - 무한_컨텍스트_학습  
aliases:  
 - InfiniTransformer  
 - Infini-Attention  
 - 무한_컨텍스트_트랜스포머  
 - 긴_시퀀스_학습  
url: https://github.com/Beomi/InfiniTransformer  
---
이 프로젝트는 "Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention" 논문을 기반으로 한 비공식 PyTorch/허깅페이스 트랜스포머 구현체입니다. 기존 트랜스포머의 컨텍스트 길이 제한을 극복하고, Llama3 및 Gemma 모델 등에서 매우 긴 시퀀스(최대 1M 토큰)를 효율적으로 처리할 수 있는 기술을 제공합니다. 두 가지 유형의 Infini-Attention(모델 전체 재설계 vs. 어텐션 레이어 단위 최적화)을 통해 메모리 효율성과 호환성을 동시에 해결하며, 다양한 데이터셋과 학습 시나리오에 적용 가능합니다.