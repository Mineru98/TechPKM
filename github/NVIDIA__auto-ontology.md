---
Language: Python
tags:
 - ontology
 - text-to-sql
 - knowledge-graph
 - MCP
 - NVIDIA
aliases:
 - Auto Ontology
 - NVIDIA Auto Ontology
 - 자동 온톨로지
url: https://github.com/NVIDIA/auto-ontology
---
NVIDIA Auto Ontology는 엔터프라이즈 메타데이터로부터 온톨로지/시맨틱 카탈로그 계층을 자동 생성하고, 에이전트에게 데이터의 위치·의미·계보(provenance) 등 신뢰할 수 있는 컨텍스트를 제공하는 오픈 라이브러리입니다. 자연어 질의를 SQL로 변환(NL-to-SQL)하여 실행하며, MCP·CLI·API를 통해 모든 에이전트 하니스에 컨텍스트를 노출할 수 있습니다. FastAPI와 Next.js 기반의 웹 UI, Postgres+pgvector, NVIDIA NIM 모델을 활용하며 Docker Compose 및 Kubernetes(Helm)로 배포할 수 있습니다.