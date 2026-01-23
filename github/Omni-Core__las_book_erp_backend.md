---
Language: Python
tags:
 - ERP
 - 도서관리
 - FastAPI
 - Docker
 - 웹애플리케이션
aliases:
 - LAS Book ERP
 - 도서ERP
 - LAS-ERP
url: https://github.com/Omni-Core/las_book_erp_backend
---
LAS Book ERP 시스템은 도서 관리를 위한 웹 애플리케이션으로, FastAPI 기반의 백엔드와 프론트엔드를 통합한 시스템입니다. Docker를 활용해 컨테이너 환경에서 실행되며, http://localhost:8000에서 접근 가능한 웹 애플리케이션과 API 문서(OpenAPI)를 제공합니다. 주요 기능으로는 도서 관리, 사용자 인증, 컨테이너 기반 배포 관리 등이 포함됩니다.  

프로젝트 구조는 백엔드(Python/FastAPI)와 프론트엔드(Vite/React)로 분리되어 있으며, 자동화된 빌드 스크립트를 통해 통합 배포가 가능합니다. Docker를 통해 개발 환경 구축과 운영 배포를 일원화하는 것이 핵심 특징입니다.