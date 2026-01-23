---
Language: JavaScript
tags:
 - 웹스크래핑
 - HTML to Markdown 변환
 - 터미널도구
 - Node.js
 - CLI
aliases:
 - Clipper.js
 - 웹콘텐츠클리퍼
 - 마크다운변환기
url: https://github.com/philschmid/clipper.js
---
Clipper는 웹 페이지 콘텐츠를 클립하여 마크다운 형식으로 변환하는 Node.js 기반 터미널 도구입니다. Mozilla의 Readability와 Turndown 라이브러리를 활용해 웹 페이지 본문을 파싱하고 마크다운으로 변환하며, 브라우저 확장 없이도 터미널에서 웹 콘텐츠를 간편하게 저장할 수 있습니다. 주로 개인 아카이빙이나 노트 작성을 위해 설계되었으며, URL 또는 로컬 HTML 파일을 입력으로 받아 처리합니다. 크롤링 기능(주의 필요)과 PDF 변환(외부 도구 연동)을 지원합니다.

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