---
Language: TypeScript
tags:
 - Evidence-Graph
 - Novel-Writing
 - TypeScript
 - Compiler
 - pnpm-workspace
aliases:
 - Novels
 - 소설 증거 그래프
 - ttsc novels
url: https://github.com/samchon/novels/blob/master/README.md
---
컴파일러(`ttsc`)와 증거 그래프(`evidence-graph`) 기술을 활용하여 영어 소설을 작성하는 실험적 프로젝트입니다. 설정, 스토리라인, 시나리오, 원고의 네 계층으로 이루어진 문서 간의 계층 구조와 인용 관계를 소스 코드처럼 엄격하게 검증하여, 문서 간의 불일치나 누락을 빌드 에러로 처리합니다. pnpm 워크스페이스 기반으로 구성되어 있으며 각 패키지가 하나의 소설 작품을 담당합니다.