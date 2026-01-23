---
Language: Python  
tags:  
 - 임베딩 모델  
 - 검색 및 RAG 도구  
 - 멀티모달  
 - 오픈소스  
 - MIT 라이선스  
aliases:  
 - BGE  
 - FlagEmbedding  
 - BAAI 일반 임베딩  
url: https://github.com/FlagOpen/FlagEmbedding  
---  
BGE(BAAI 일반 임베딩)는 검색 증강 생성(RAG) 및 검색 작업을 위한 통합 툴킷입니다. 다양한 기능(밀집 검색, 희소 검색, 멀티벡터 검색)과 다국어 지원(100개 이상 언어), 입력 길이(최대 8192토큰)를 제공하며, MTEB 및 MIRACL 벤치마크에서 SOTA 성능을 달성했습니다. Python 기반 오픈소스 라이브러리로, 임베딩 생성, 재순위 지정, 파인튜닝 기능을 포함하며, MIT 라이선스로 상업적으로 자유롭게 사용 가능합니다.  

```python
# 예제 코드: BGE 모델 로드 및 임베딩 생성
from FlagEmbedding import FlagAutoModel  
model = FlagAutoModel.from_finetuned('BAAI/bge-base-en-v1.5', query_instruction_for_retrieval="Represent this sentence for searching relevant passages:")
embeddings = model.encode(["I love NLP", "I love machine learning"])
```