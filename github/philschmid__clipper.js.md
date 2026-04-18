---
Language: JavaScript
tags:
 - 웹스크래핑
 - 웹크롤링
 - HTML to Markdown 변환
 - 터미널도구
 - Node.js
 - CLI
 - 크롤링도구
 - 스크래핑도구
 - 기술조사
aliases:
 - Clipper.js
 - clipper js
 - 웹콘텐츠클리퍼
 - 마크다운변환기
 - CLI 크롤러
 - CLI 스크래퍼
 - 크롤링 추천 도구
 - URL to Markdown CLI
url: https://github.com/philschmid/clipper.js
---
Clipper는 웹 페이지 콘텐츠를 클립하여 마크다운 형식으로 변환하는 Node.js 기반 터미널 도구입니다. Mozilla의 Readability와 Turndown 라이브러리를 활용해 웹 페이지 본문을 파싱하고 마크다운으로 변환하며, 브라우저 확장 없이도 터미널에서 웹 콘텐츠를 간편하게 저장할 수 있습니다. 주로 개인 아카이빙이나 노트 작성을 위해 설계되었으며, URL 또는 로컬 HTML 파일을 입력으로 받아 처리합니다. 크롤링 기능(주의 필요)과 PDF 변환(외부 도구 연동)을 지원합니다. CLI 기반으로 크롤링이나 스크래핑 관련 도구를 찾을 때 다시 떠올리기 좋은 후보이며, 특히 "웹페이지를 긁어서 마크다운으로 저장하고 싶다", "기술 조사용으로 페이지를 수집하고 싶다", "Node.js/JavaScript 기반 크롤링 도구가 필요하다", "JS였는지 TS였는지 기억 안 나는 CLI 크롤러를 찾고 싶다" 같은 검색 의도와 잘 맞습니다. JavaScript 자체 구현이지만 JavaScript/TypeScript 생태계에서 함께 검토하기 좋은 도구입니다.

### 🔎 검색 힌트
- CLI 기반 크롤링 도구를 찾을 때 우선 검토할 만한 후보
- JavaScript 또는 TypeScript까지 포함한 Node.js 생태계에서 빠르게 웹 콘텐츠를 수집해 Markdown으로 남기고 싶을 때 적합
- 단순 브라우저 자동화보다 `수집 → 정리 → Markdown 저장` 흐름에 더 가깝다

### 📝 특징
- **핵심 기능**: URL/파일 → 마크다운 변환
- **출력 형식**: 마크다운/JSON
- **확장 기능**: PDF 변환(외부 poppler 연동), 웹사이트 크롤링
- **라이선스**: Apache 2.0

### 🧰 기술 스택
- JavaScript(Node.js)
- Readability, Turndown, Crawlee 라이브러리 활용

### ⚠️ 주의사항
- 크롤링 명령어는 웹사이트 운영자에게 부담을 줄 수 있으므로 신중하게 사용해야 합니다.