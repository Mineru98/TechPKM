---
Language: Rust
tags:
 - ray-tracing
 - threejs
 - path-tracing
 - game-engine
 - webgpu
aliases:
 - ThreeRT
 - threert
 - 하드웨어 레이 트레이싱 three.js
url: https://github.com/meshy-dev/ThreeRT
---
ThreeRT는 three.js 스타일의 API 뒤에서 하드웨어 레이 트레이싱 기반 실시간 패스 트레이싱을 수행하는 엔진입니다. three.js로 씬을 작성하면 모든 조명이 GPU의 레이 트레이싱 하드웨어로 추적되어 60fps로 렌더링되며, 그림자 맵·라이트맵·베이킹 없이 물리 단위 기반의 사실적인 빛을 제공합니다. Rust와 wgpu로 작성된 렌더러를 핵심으로, 게임 런타임, 복셀 파괴 시스템, macOS/iOS 클라이언트를 갖춘 MeshyAI의 리서치 프로젝트입니다.