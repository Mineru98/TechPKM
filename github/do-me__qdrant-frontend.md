---
Language: JavaScript
tags:
 - qdrant
 - vector-search
 - frontend-ui
 - transformers.js
 - CORS
aliases:
 - qdrant-frontend
 - 벡터검색프론트엔드
 - qdrant-table-ui
 - 브라우저임베딩
url: https://github.com/do-me/qdrant-frontend
---
Qdrant 벡터 검색을 위한 브라우저 기반 프론트엔드입니다. Transformers.js를 활용해 모델 추론을 클라이언트 측에서 직접 수행하며, Qdrant 컬렉션에 대한 검색 쿼리를 간편하게 실행할 수 있습니다. 로컬 또는 원격 Qdrant 서버에 연결 가능하며, CORS 설정이 필요한 환경에서는 프록시 구성이 요구됩니다. 검색 모델 선택, 결과 행 제한 등 사용자 정의 기능을 지원합니다.

이 프로젝트는 Qdrant 웹 UI의 한계를 보완하기 위해 제작되었으며, 별도의 인퍼런싱 서버 없이 정적 페이지만으로 벡터 검색 인터페이스를 제공합니다. UI 개선, Qdrant JS 클라이언트 통합, 차원 축소 기능 추가 등의 향후 개선 계획이 있습니다.