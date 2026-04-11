---
Language: Ruby
tags:
 - Logstash
 - Nori
 - 형태소 분석
 - Elasticsearch
 - 한국어 처리
aliases:
 - Nori 필터 플러그인
 - logstash-filter-nori
 - Logstash Nori
url: https://github.com/twosom/logstash-filter-nori/blob/main/readme.md
---
Logstash를 위한 형태소 분석 필터 플러그인으로, Apache Lucene의 Nori 분석기를 기반으로 한국어 텍스트에서 원하는 품사의 형태소를 추출합니다. 사용자 사전을 지원하며, 추출된 형태소는 지정된 필드에 배열 형태로 저장되어 로그 데이터의 한국어 자연어 처리에 활용됩니다.