---
Language: JavaScript
tags:
 - 이미지비교
 - 픽셀매칭
 - 시각적회귀테스트
 - Node.js
 - 브라우저
aliases:
 - pixelmatch
 - 픽셀매치
url: https://github.com/mapbox/pixelmatch/blob/main/README.md
---
원래 테스트 환경에서 스크린샷을 비교하기 위해 만들어진, 가장 작고 단순하며 빠른 JavaScript 픽셀 수준 이미지 비교 라이브러리입니다. 외부 의존성 없이 150줄 이하의 코드로 작성되었으며, 원시 타입 배열을 직접 다루기 때문에 Node.js와 브라우저 등 모든 환경에서 매우 빠르게 동작합니다. 정확한 안티앨리어싱 픽셀 감지와 지각적 색상 차이 측정 메트릭을 주요 특징으로 제공합니다.