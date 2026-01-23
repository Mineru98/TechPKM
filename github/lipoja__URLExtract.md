---
Language: Python
tags:
 - URL 추출
 - TLD 기반
 - 텍스트 처리
aliases:
 - URLExtract
 - URL 추출기
 - TLD 검색
url: https://github.com/lipoja/URLExtract
---
URLExtract는 텍스트에서 TLD(최상위 도메인)를 기반으로 URL을 추출하는 Python 라이브러리입니다. 주어진 텍스트에서 유효한 도메인 이름을 인식하고, 정규화된 URL을 반환합니다. DNS 검증 옵션을 통해 잘못된 도메인 필터링도 가능하며, 최신 TLD 목록을 자동으로 업데이트합니다.  

이 프로젝트는 텍스트 분석, 소셜 미디어 모니터링, 웹 스크래핑 등 URL 감지가 필요한 시나리오에 최적화되어 있습니다. `find_urls`, `gen_urls`, `has_urls` 등의 API를 제공하며, CSS/JS 코드에서 발생하는 오검출 가능성에 대한 주의 사항이 문서화되어 있습니다. MIT 라이선스로 배포됩니다.