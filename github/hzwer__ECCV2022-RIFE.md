---
Language: Python
tags:
 - video-frame-interpolation
 - optical-flow
 - deep-learning
 - computer-vision
 - pytorch
aliases:
 - RIFE
 - ECCV2022-RIFE
 - Real-Time Intermediate Flow Estimation
 - 비디오 프레임 보간
url: https://github.com/hzwer/ECCV2022-RIFE
---
RIFE는 ECCV 2022에 게재된 "Real-Time Intermediate Flow Estimation for Video Frame Interpolation" 논문의 공식 구현 프로젝트이다. 2080Ti GPU에서 720p 2배 보간을 30FPS 이상으로 처리할 수 있으며, 두 이미지 사이의 임의 시점(timestep) 프레임 보간을 지원한다. CLI 및 Docker 환경에서 비디오/이미지 보간을 수행할 수 있고, 애니메이션 장면에 최적화된 최신 모델은 Practical-RIFE 저장소에서 제공된다.