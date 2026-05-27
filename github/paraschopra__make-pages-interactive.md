---
Language: Python, JavaScript
tags:
 - HTML
 - Claude-Code
 - 피드백
 - 인터랙티브
 - 정적-페이지
aliases:
 - make-pages-interactive
 - 페이지 인터랙티브 스킬
 - HTML 피드백 시스템
url: https://github.com/paraschopra/make-pages-interactive/blob/main/README.md
---
정적 HTML 페이지 모음을 즉각적인 피드백과 댓글을 남길 수 있는 인터랙티브 표면으로 전환해 주는 Claude Code 스킬입니다. 사용자는 페이지 내의 텍스트를 하이라이트하거나 특정 요소를 클릭하여 코멘트를 남길 수 있으며, 이 내용은 로컬 수신함(inbox)에 저장되어 Claude가 즉시 인식하고 HTML을 직접 수정하는 방식으로 작동합니다.

주로 긴 리서치 보고서, 디자인 문서, 생성된 대시보드 등 HTML 형태의 산출물을 반복적으로 검토하고 수정해야 하는 환경에서 유용하게 사용할 수 있습니다. Python 표준 라이브러리로 작성된 가벼운 HTTP 서버와 JavaScript 클라이언트 라이브러리로 구성되어 있으며, 프로세스 누수를 방지하기 위한 자동 종료 및 유휴 시간 타임아웃 기능이 기본적으로 제공됩니다.