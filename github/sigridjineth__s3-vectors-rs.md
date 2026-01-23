---
Language: Rust  
tags:  
 - AWS S3  
 - 벡터 데이터베이스  
 - RAG(Retrieval-Augmented Generation)  
 - CLI 도구  
 - 임베딩 처리  
aliases:  
 - s3-vectors-rs  
 - AWS 벡터 저장소  
 - RAG CLI 도구  
 - S3 벡터 관리  
url: https://github.com/sigridjineth/s3-vectors-rs  
---  
AWS S3를 활용한 벡터 저장소 관리를 위한 비공식 Rust 기반 CLI 도구입니다. RAG(Retrieval-Augmented Generation) 기능을 지원하여 문서 임베딩, 유사도 검색 및 자연어 쿼리가 가능합니다. 버킷/인덱스/벡터 관리, 배치 처리, 정책 설정 등의 핵심 기능을 제공하며, 현재 `all-MiniLM-L6-v2` 모델을 사용한 텍스트 임베딩과 코사인/유클리드 거리 기반 검색이 지원됩니다.