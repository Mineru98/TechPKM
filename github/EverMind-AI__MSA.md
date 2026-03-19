---
Language: Python
tags:
 - MSA
 - Long-Context
 - Sparse Attention
 - RAG
 - LLM
aliases:
 - Memory Sparse Attention
 - MSA Framework
 - Long-context LLM
url: https://github.com/EverMind-AI/MSA
---
MSA(Memory Sparse Attention)는 1억 토큰 이상의 극한 긴 문맥을 처리하기 위해 설계된 end-to-end 학습이 가능한 희소 잠재 메모리 프레임워크입니다. 문서 단위 RoPE와 계층적 라우팅을 통해 훈련과 추론에서 거의 선형적인 복잡도를 달성하며, 기존 RAG나 하이브리드 어텐션 방식이 가진 정확도 저하 문제를 해결합니다. 결과적으로 MSA는 16K에서 100M 토큰으로 확장됨에도 9% 미만의 성능 저하만을 보이며 메모리 용량과 추론 능력의 분리를 실현합니다.