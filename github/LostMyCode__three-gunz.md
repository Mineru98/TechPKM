---
Language: C++
tags:
 - WebGL
 - WebAssembly
 - GamePorting
 - Three.js
 - GunZ
aliases:
 - GunZ The Duel Web Version
 - GunZ Browser Port
 - Three-GunZ
url: https://github.com/LostMyCode/three-gunz
---
이 프로젝트는 고전 TPS 게임인 'GunZ The Duel'을 웹 브라우저에서 실행 가능하도록 완전히 포팅한 시도입니다. 초기에는 Three.js를 활용하여 맵과 모델을 렌더링하는 것에서 시작했으나, Emscripten과 WebAssembly를 통해 원본 클라이언트와 서버를 웹에서 구동하는 단계까지 발전했습니다. D3D9를 WebGL로 변환하고 IndexedDB를 통해 파일 시스템을 에뮬레이션하여, 별도의 설치 과정 없이 브라우저만으로 즉시 플레이할 수 있는 것이 특징입니다.