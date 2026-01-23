---
Language: Python
tags:
 - Decompilation
 - Binary Analysis
 - Large Language Models
 - Reverse Engineering
 - Ghidra
aliases:
 - LLM4Decompile
 - 바이너리 디컴파일
 - 이진 코드 역공학
 - 소스 코드 복원
url: https://github.com/albertan017/LLM4Decompile
---
LLM4Decompile은 Linux x86_64 바이너리를 인간 친화적 C 소스 코드로 변환하는 오픈소스 LLM 프로젝트입니다. GCC 최적화 레벨(O0~O3)을 지원하며, Ghidra의 의사 코드를 정제하는 "LLM4Decompile-Ref"와 바이너리를 직접 디컴파일하는 "LLM4Decompile-End" 두 가지 접근 방식을 제공합니다. 1.3B~33B 파라미터 규모의 모델들을 Hugging Face에서 공개하며, 재실행 가능성(re-executability)을 주요 평가 지표로 사용합니다. HumanEval-Decompile 및 ExeBench 벤치마크를 통해 검증된 역공학 솔루션입니다.