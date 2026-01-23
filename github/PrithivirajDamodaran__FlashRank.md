---
Language: Python  
tags:  
 - 검색 재순위화  
 - NLP  
 - RAG  
 - 경량 모델  
 - 오픈소스 라이브러리  
aliases:  
 - FlashRank  
 - 플래시랭크  
 - 검색 재랭킹  
 - Reranker  
url: https://github.com/castorini/flashrank  
---
검색 결과를 LLM에 전달하기 전에 최첨단 Pairwise 또는 Listwise 재순위화 모델로 재정렬할 수 있는 초경량 초고속 Python 라이브러리입니다. Torch/Transformers 없이도 CPU에서 실행 가능며, 4MB 크기의 최소 재순위화 모델을 포함한 다양한 모델을 지원합니다. RAG 파이프라인, 벡터 검색, 하이브리드 검색 등에 통합하여 검색 결과 정확도를 향상시키는 데 최적화되어 있습니다. Apache 2.0 라이선스로 배포됩니다.