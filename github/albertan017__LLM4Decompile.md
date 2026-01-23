---
Language: Python  
tags:  
 - Binary Decompilation  
 - Large Language Models  
 - Reverse Engineering  
 - C Source Code  
 - Ghidra Integration  
aliases:  
 - LLM4Decompile  
 - SK²Decompile  
 - Binary-to-Source  
 - Ghidra Refinement  
 - Decompile Benchmark  
url: https://github.com/albertan017/LLM4Decompile  
---
LLM4Decompile은 바이너리 코드를 인간이 읽을 수 있는 C 소스 코드로 역컴파일하는 오픈소스 대형 언어 모델 프로젝트입니다. 이 프로젝트는 Linux x86_64 바이너리를 대상으로 GCC 최적화 수준(O0~O3)을 지원하며, Ghidra와 같은 기존 도구의 결과를 개선하는 두 가지 주요 모델(End-to-End 및 Refine)을 제공합니다. 다양한 파라미터 크기(1.3B~33B)의 모델과 평가 지표(재실행 가능성)를 통해 성능을 검증하며, 200만 개의 바이너리-소스 페어 데이터셋을 활용한 훈련 인프라를 구축했습니다. 역컴파일 분야의 선제적 연구로서 아키텍처와 설정 확장성을 지속적으로 개선하고 있습니다.