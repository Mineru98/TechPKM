---
Language: JavaScript
tags:
 - 실시간 PDF 뷰어
 - WebSocket
 - PDF.js
 - Node.js
 - Docker
aliases:
 - 실시간 PDF 공유
 - PDF.js 동기화 뷰어
 - WebSocket 기반 PDF 뷰어
url: https://github.com/user-attachments/assets/03670358-7d36-493e-af82-b8f14db7cf77
---
이 프로젝트는 PDF.js와 WebSocket을 활용해 실시간으로 PDF를 공유하는 웹 애플리케이션입니다. 호스트가 업로드한 PDF를 참가자들이 실시간으로 동기화하여 볼 수 있으며, 화질 저하 없이 벡터 그래픽을 그대로 렌더링합니다. Node.js 기반 백엔드와 Docker 배포 기능을 지원하여 로컬 개발 및 클라우드 배포가 모두 가능합니다.  

호스트는 PDF 업로드 및 페이지 제어가 가능하고, 참가자는 호스트의 페이지 이동을 실시간으로 따라가는 양방향 통신 구조를 갖추고 있습니다. MIT 라이선스로 배포되는 오픈소스 프로젝트입니다.