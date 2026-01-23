---
Language: Python  
tags:  
 - 비동기 API  
 - DC인사이드  
 - 웹 크롤링  
aliases:  
 - dcinside 크롤링  
 - 비동기 갤러리 API  
url: https://github.com/eunchuldev/dcinside-python3-api  
---  
# dcinside-python3-api  
DC인사이드 갤러리의 글과 댓글을 크롤링하고, 글/댓글 작성, 수정, 삭제 기능을 제공하는 비동기 API 라이브러리입니다. Python 3.6 이상에서 동작하며, 비동기 방식으로 갤러리 데이터를 효율적으로 처리할 수 있습니다. 주요 기능으로는 글 목록 조회, 본문/이미지/댓글 수집, 글 작성/수정/삭제, 댓글 작성 등이 포함됩니다.  

- **핵심 기능**:  
  - 갤러리 글 크롤링 및 무한 스크롤 지원  
  - 글 본문, 이미지, 댓글 수집  
  - 글/댓글 작성, 수정, 삭제  
  - 이미지 다운로드 및 로컬 저장  
- **지원 환경**: Linux/Windows/macOS 호환  
- **사용 예시**: 프로그래밍 갤러리 글 제목 크롤링, 특정 문서 이미지 수집, 자동 댓글 작성 등  

> `aiohttp`, `lxml` 의존성 필요. `pip install dc_api`로 설치 가능.