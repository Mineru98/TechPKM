---
Language: C++
tags:
 - WebGL
 - Emscripten
 - Direct3D9
 - WebAssembly
 - Graphics
aliases:
 - d3d9-webgl
 - D3D9 to WebGL
url: https://github.com/LostMyCode/d3d9-webgl
---
이 프로젝트는 Direct3D 9 고정 기능 파이프라인(Fixed-Function Pipeline)을 WebGL 2.0으로 구현하여 레거시 C++ 게임이나 애플리케이션을 수정 없이 웹 브라우저에서 실행할 수 있게 해주는 호환 계층입니다. Emscripten과 WebAssembly를 통해 빌드되며, 단일 `.cpp` 파일과 헤더만으로 기존 D3D9 API 호출을 WebGL 명령어로 자동 변환합니다. 주요 기능으로는 텍스처 처리, 조명, 안개, 렌더 타겟 등의 D3D9 상태를 완벽하게 에뮬레이션하며, GunZ: The Duel과 같은 고전 온라인 게임의 브라우저 포팅에 실제로 활용되었습니다.