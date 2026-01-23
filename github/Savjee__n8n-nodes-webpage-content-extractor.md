---
Language: JavaScript
tags:
 - n8n 커뮤니티노드
 - 웹컨텐츠 추출
 - Readability
aliases:
 - 웹페이지 콘텐츠 추출기
 - n8n Readability 노드
url: https://github.com/Savjee/n8n-nodes-webpage-content-extractor
---
이 프로젝트는 n8n 커뮤니티노드로, 주어진 URL에서 헤더를 제외한 본문 콘텐츠를 추출하는 기능을 제공합니다. Mozilla의 Readability 라이브러리를 기반으로 구현되어 브라우저의 리더 모드와 유사한 결과를 생성합니다. HTTP 요청 노드와 연계하여 웹 페이지의 주요 콘텐츠를 효율적으로 파싱할 수 있습니다.

### 요약
n8n 환경에서 웹 페이지의 광고/헤더/푸터 등을 제외한 순수 본문 콘텐츠를 추출하는 커뮤니티노드입니다. Firefox 리더 뷰와 동일한 Readability 알고리즘을 적용하였으며, HTTP 요청 노드와의 연동을 통해 다양한 웹 사이트 데이터를 처리할 수 있습니다. JavaScript 기반 구현으로 n8n v1.20.0 이상에서 호환됩니다.