---
Language: JavaScript
tags:
 - PubSubHubbub
 - YouTube API
 - 실시간 알림
 - 영상 관리 서버
 - NodeJS
aliases:
 - youtube-pubsub-callback
 - 애니멀봄 알림 서버
 - moaon-video-sync
url: https://github.com/OzRagwort/youtube-pubsub-callback-server
---
이 프로젝트는 YouTube PubSubHubbub 프로토콜을 활용해 채널 구독 알림을 실시간으로 수신하는 NodeJS 서버입니다. 수신된 영상 업로드/수정/삭제 이벤트를 [애니멀봄 서버](https://github.com/OzRagwort/moaon-server)에 전달하여 영상 데이터를 최신 상태로 유지하는 것이 핵심 목적입니다. XML 피드 파싱과 주기적 구독 갱신을 통해 안정적인 실시간 동기화를 구현합니다.