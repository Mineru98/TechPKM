---
Language: Python  
tags:  
 - RAG(검색증강생성)  
 - 지식그래프  
 - 로컬AI  
 - Ollama  
 - DeepSeek  
aliases:  
 - DeepSeek RAG 챗봇  
 - GraphRAG 통합  
 - 로컬 PDF 분석기  
url: https://github.com/SaiAkhil066/DeepSeek-RAG-Chatbot  
---  
이 프로젝트는 PDF, DOCX, TXT 파일에서 정보를 검색·생성하는 로컬 기반 RAG(Retrieval-Augmented Generation) 챗봇입니다. DeepSeek-7B 모델과 BM25·FAISS 하이브리드 검색, 지식그래프(GraphRAG), 대화 기록 통합, 신경 재랭킹(Neural Reranking) 등을 결합해 정확한 문맥 이해를 제공합니다. 오프라인 환경에서 작동하며 사용자 정의 UI와 다양한 설치 옵션(스크립트/수동/도커)을 지원합니다.  

> 🔍 **핵심 기능**:  
> - Hybrid Retrieval(BM25+FAISS) + GraphRAG로 문서 관계성 분석  
> - 대화 기록 기반 맥락 유지 및 쿼리 확장(HyDE)  
> - 로컬 설치(오프라인) 및 크로스 플랫폼 호환성  
> - Ollama 모델(DeepSeek/Qwen 등) 호환 및 확장 가능한 RAG 파이프라인