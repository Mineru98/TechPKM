---
Language: JavaScript
tags:
 - agent-skill
 - 3D-애니메이션
 - 비디오-렌더링
 - isometric
 - exploded-view
aliases:
 - Anatomy Reveal
 - anatomy-reveal-skill
 - 해부도 리빌
url: https://github.com/annnguyentt/anatomy-reveal-skill
---
Anatomy Reveal은 사진이나 객체 이름만으로 어떤 물건이든 아이소메트릭 해부도(잉크 드로잉 스타일의 작은 볼록 파트들)로 재구성하는 AI 에이전트 스킬입니다. 결과물은 드래그로 회전하고 호버로 분해할 수 있는 인터랙티브 해부 페이지와, 객체가 등장해 부분 확대, 기능 시연, 분해 후 재조립을 보여주는 MP4 리빌 필름(다양한 종횡비, 3~60초) 두 가지로 제공됩니다. Node.js, Chrome, ffmpeg, ImageMagick을 활용해 렌더링하며, 에스프레소 머신 예제(82개 파트)가 포함되어 있습니다.