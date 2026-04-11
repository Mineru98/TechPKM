---
Language: Python
tags:
 - 3D-Object-Detection
 - Computer-Vision
 - Open-Vocabulary
 - Point-Cloud
 - Bounding-Box
aliases:
 - Boxer
 - BoxerNet
 - 2D to 3D Bounding Box Lifting
url: https://github.com/facebookresearch/boxer/blob/main/README.md
---
Boxer는 오픈 월드 환경에서 2D 바운딩 박스를 정적이고 글로벌하게 융합된 3D 바운딩 박스(OBB)로 변환(Lifting)하는 프로젝트입니다. 카메라 포즈 정보와 반밀도(semi-dense) 포인트 클라우드를 활용하여 실내 객체 탐지에 중점을 둡니다. 제공되는 사전 학습 모델과 다양한 데이터셋(Project Aria, CA-1M, SUN-RGBD, ScanNet)에 대한 추론 코드를 통해 3D 객체 탐지 및 온라인 추적, 오프라인 융합을 수행할 수 있습니다.