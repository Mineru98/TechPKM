---
Language: C++
tags:
 - NeRF
 - CUDA
 - 3D 렌더링
 - 머신러닝
 - 실시간 그래픽스
aliases:
 - instant-ngp
 - NVIDIA Instant Neural Graphics Primitives
 - 실시간 뉴럴 그래픽스
url: https://github.com/NVlabs/instant-ngp
---
NVIDIA에서 개발한 이 프로젝트는 다중 해상도 해시 인코딩을 활용한 실시간 뉴럴 그래픽스 프리미티브 도구입니다. NeRF(신경 방사장), SDF(유부호 거리 함수), 뉴럴 이미지 및 뉴럴 볼륨 렌더링을 5초 이내에 처리할 수 있으며, tiny-cuda-nn 프레임워크를 기반으로 고성능 CUDA 연산을 지원합니다. 대화형 GUI와 VR 모드를 통해 3D 모델과 장면을 실시간으로 탐색 및 편집할 수 있으며, 다양한 데이터셋과 호환됩니다. SIGGRAPH 2022에 발표된 논문을 기반으로 제작되었습니다.