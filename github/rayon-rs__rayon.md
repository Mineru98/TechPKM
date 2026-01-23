---
Language: Rust  
tags:  
 - 병렬처리  
 - 데이터 병렬성  
 - 러스트 라이브러리  
 - 병렬 반복자  
 - 멀티스레딩  
aliases:  
 - Rayon  
 - 러스트 병렬처리  
 - Rayon 라이브러리  
 - Rayon-RS  
url: https://github.com/rayon-rs/rayon  
---  
Rayon은 Rust를 위한 데이터 병렬성 라이브러리로, 순차적 계산을 병렬화하는 것을 쉽게 만들어주며 데이터 레이스 프리덤을 보장합니다. 병렬 반복자(par_iter)를 통해 코드 변경 최소화만으로 자동 병렬 처리가 가능하며, 스레드 풀 커스터마이징 및 join/scope 함수를 통한 유연한 병렬 작업 관리가 특징입니다. 웹어셈블리 환경에서도 동작하며, MIT/Apache 2.0 듀얼 라이선스로 배포됩니다.