---
Language: JavaScript
tags:
 - n8n 커뮤니티 노드
 - 웹 콘텐츠 추출
 - Readability
 - 웹 스크래핑
 - Mozilla
aliases:
 - n8n 웹 추출기
 - 웹페이지 리더
- webpage-content-extractor
url: https://github.com/n8n-io/n8n-nodes-webpage-content-extractor
---
이 프로젝트는 주어진 URL에서 브라우저의 '리더 모드'와 유사하게 광고 배너, 헤더/푸터 등을 제외한 본문 콘텐츠를 추출하는 n8n 커뮤니티 노드입니다. Firefox 리더 뷰에서 사용되는 Readability 라이브러리를 기반으로 구현되었으며, HTTP 요청 노드와 연동해 웹 페이지의 정제된 텍스트를 얻을 수 있습니다. n8n v1.20.0 이상에서 사용 가능하며, 커스텀 HTTP 설정(인증/헤더 등)을 지원합니다.