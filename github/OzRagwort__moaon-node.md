---
Language: JavaScript
tags:
 - PubSubHubbub
 - Youtube API
 - 실시간 알림
 - NodeJS 서버
 - 영상 관리
aliases:
 - 유튜브 구독 알림 서버
 - moaon-node
 - 애니멀봄 알림 서버
url: https://github.com/OzRagwort/moaon-node
---
이 프로젝트는 YouTube의 PubSubHubbub 프로토콜을 활용하여 채널 영상 변경 사항을 실시간으로 수신하는 NodeJS 서버입니다. 구독한 채널의 영상 업로드/수정/삭제 이벤트를 감지하고, 이를 기반으로 [애니멀봄 서버](https://github.com/OzRagwort/moaon-server)의 데이터를 최신 상태로 유지합니다. YouTube API와 연동하여 실시간 알림 시스템을 구현하며, 주기적으로 구독 목록을 갱신하는 기능을 포함합니다. 영상 메타데이터 처리 및 외부 서버와의 연동을 통해 효율적인 콘텐츠 관리 체계를 제공합니다.