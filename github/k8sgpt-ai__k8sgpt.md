---
Language: Go  
tags:  
 - Kubernetes  
 - AI 분석 도구  
 - 클러스터 진단  
 - SRE  
 - LLM 통합  
aliases:  
 - k8sgpt  
 - 쿠버네티스 AI 진단  
 - Kubernetes 문제 해결  
 - 쿠버네티스 분석 도구  
url: https://github.com/k8sgpt-ai/k8sgpt  
---
`k8sgpt`는 쿠버네티스 클러스터를 스캔하고 영어로 문제를 진단 및 분류하기 위한 도구입니다. SRE 경험을 분석기에 코드화하여 AI로 보강된 관련 정보를 추출하며, OpenAI, Azure, Cohere 등 다양한 LLM 백엔드와 통합됩니다. 클러스터 상태 분석, 문서 연동, 사용자 정의 분석기 확장 기능을 제공하며, CLI 또는 MCP 서버 모드로 사용할 수 있습니다.  

핵심 기능은 다음과 같습니다:  
1. **다양한 리소스 분석기** (Pod, Service, Node 등)  
2. **AI 기반 문제 설명** (`--explain` 플래그)  
3. **데이터 익명화** (민감 정보 보호)  
4. **로컬/클라우드 AI 백엔드 지원**  
5. **MCP 서버**를 통한 Claude Desktop 등 도구와 통합 가능  

설치 및 사용법은 README의 [Quick Start](#quick-start) 섹션을 참조하세요. 공식 문서는 [https://docs.k8sgpt.ai](https://docs.k8sgpt.ai)에서 제공됩니다.