---
Language: Swift
tags:
 - macOS
 - semantic-search
 - multimodal-embedding
 - llama.cpp
 - local-search
aliases:
 - DigUp
 - DigUp Mac 검색
 - EmbeddingGemma 2 검색 앱
url: https://github.com/ARahim3/DigUp
---
DigUp는 Google DeepMind의 멀티모달 임베딩 모델 EmbeddingGemma 2를 활용해 Mac의 파일을 내용 기반으로 검색하는 무료 오픈소스 macOS 앱입니다. 사진, PDF, 문서, 오디오, 비디오를 로컬에서 인덱싱하여 "해변의 개"처럼 자연어로 묘사하면 파일 종류에 관계없이 해당 페이지나 순간으로 바로 이동할 수 있으며, 100개 이상의 언어를 지원하고 모든 처리가 Mac에서 완전히 오프라인으로 이루어져 프라이버시를 보장합니다. `code:` 접두사를 통한 코드 검색도 제공하며, llama.cpp(Metal)와 SQLite 벡터 인덱스 기반으로 동작합니다.