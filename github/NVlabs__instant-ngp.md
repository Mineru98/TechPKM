---
Language: C++
tags:
 - NeRF
 - 컴퓨터 비전
 - 3D 렌더링
 - 머신러닝
 - CUDA
aliases:
 - Instant-NGP
 - Instant Neural Graphics Primitives
 - Multi-resolution Hash Encoding
url: https://github.com/NVlabs/instant-ngp
---
NVlabs의 Instant-NGP 프로젝트는 다해상도 해시 인코딩을 기반으로 한 즉각적 신경망 그래픽 프리미티브를 구현한 오픈소스 도구입니다. NeRF(Neural Radiance Fields), SDF(Signed Distance Functions), 신경 이미지, 신경 볼륨 등 4가지 그래픽 프리미티브를 초고속(5초 이내)으로 학습/렌더링할 수 있으며, CUDA 기반 고속 처리 라이브러리 tiny-cuda-nn을 활용합니다. 대화형 GUI, VR 지원, 카메라 경로 편집, 다양한 데이터셋 호환성 등을 제공하여 연구 및 콘텐츠 제작에 유용합니다. SIGGRAPH 2022에서 발표된 논문으로 이론적 기반을 갖추었습니다.