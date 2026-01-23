---
Language: Python
tags:
 - 유튜브 임베드
 - Nix
 - Gunicorn
 - GitHub 마크다운
 - 정적 이미지 오버레이
aliases:
 - 유튜브 이미지 오버레이
 - yt-embed
 - GitHub 유튜브 임베더
url: https://github.com/example/yt-embed
---
이 프로젝트는 GitHub 마크다운에서 유튜브 동영상을 임베드할 때 시각적 단서를 제공하는 정적 이미지 오버레이를 생성하는 도구입니다. 기존 유튜브 썸네일 링크에 플레이 버튼을 추가하여 동영상임을 명확히 나타내는 시각적 큐를 자동 생성합니다. Nix 패키지 관리자와 Gunicorn 서버로 구동되며, `https://yt-embed.live/embed?v=VIDEO_ID` 형식의 URL로 접근 가능합니다. systemd 서비스와 Nginx 설정 예시를 통해 지속적인 호스팅이 가능하도록 설계되었습니다.