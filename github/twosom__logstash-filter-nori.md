---
Language: Ruby  
tags:  
 - text-analysis  
 - logstash-filter  
 - korean-nlp  
 - morphological-analysis  
 - user-dictionary  
aliases:  
 - logstash nori 필터  
 - Nori 토크나이저  
 - 한국어 형태소 분석  
 - logstash-filter-nori  
url: https://github.com/twosom/logstash-filter-nori  
---  
Logstash를 위한 한국어 형태소 분석 필터 플러그인입니다. Lucene Nori 분석기를 기반으로 하여 텍스트를 형태소 단위로 분해하며, 사용자 사전 적용이 가능합니다. 로그 데이터에서 명사(NNG/NNP) 등의 품사를 추출하는 데 특화되어 있습니다.  

이 플러그인은 Logstash 8.2.2 이상 버전에서 직접 설치 가능하며, 이전 버전에서는 수동으로 빌드한 gem 파일로 설치해야 합니다. 필터 설정 시 분석 대상 필드와 추출할 품사 태그를 지정할 수 있습니다.