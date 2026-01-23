---
Language: JavaScript
tags:
 - OpenCV
 - WebAssembly
 - 이미지처리
 - node.js
 - deno
aliases:
 - OpenCV-Wasm
 - OpenCV WebAssembly
 - 웹어셈블리 OpenCV
 - 자바스크립트 OpenCV
url: https://github.com/echamudi/opencv-wasm
---
OpenCV-Wasm은 JavaScript + WebAssembly로 사전 컴파일된 OpenCV 라이브러리로, node.js 및 Deno 환경에서 OpenCV 설치 없이 이미지 처리 기능을 제공합니다. 전체 OpenCV 라이브러리가 `opencv.js`와 `opencv.wasm` 파일에 포함되어 있으며, 종속성이 없는 것이 특징입니다. 딜레이션, 템플릿 매칭 등 다양한 컴퓨터 비전 작업을 수행할 수 있습니다.

이 프로젝트는 OpenCV.js와 동일한 API를 유지하면서 동기식 로딩 방식을 채택하여 웹 개발자들이 쉽게 사용할 수 있도록 설계되었으며, 예제 코드와 테스트 스크립트를 통해 사용법을 명확히 설명합니다. BSD-3-Clause 라이선스로 배포됩니다.