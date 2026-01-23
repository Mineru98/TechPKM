---
Language: Python  
tags:  
 - YouTube 댓글 분석  
 - Python 스크립트  
 - 자동 알림 시스템  
 - Google API  
 - 오픈소스 도구  
aliases:  
 - 유튜브 댓글 감지기  
 - YCD  
 - 댓글 간격 검출기  
url: https://github.com/Undecember/YoutubeCommentDetector  
---
이 프로젝트는 특정 유튜브 영상의 댓글창에 일정 시간(1분 이상) 추가 댓글이 없는 기간을 감지하는 Python 기반 도구입니다. [지정된 이벤트 영상](https://youtu.be/_gKmYOLKQBg)의 최근 댓글을 수집하고, 인접 댓글 사이의 시간 간격을 분석하여 결과를 설정된 이메일 주소로 보고하는 기능을 제공합니다. Google API를 활용한 인증 및 데이터 페칭이 핵심 기술 스택이며, 지속적인 댓글 활동이 없는 구간을 효율적으로 식별합니다.