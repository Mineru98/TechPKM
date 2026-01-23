---
Language: Python
tags:
 - 3D_객체_감지
 - 딥러닝
 - 컴퓨터비전
 - KITTI_데이터셋
 - 실시간_시스템
aliases:
 - AutoShape
 - AutoShape_3D_감지
 - 실시간_모양_인식
 - 단안_3D_감지
url: https://github.com/zongdai/AutoShape
---
AutoShape는 ICCV 2021에서 소개된 단안 카메라를 이용한 실시간 3D 객체 감지 프레임워크로, 객체 형태를 인식하는 데 중점을 둡니다. KITTI 데이터셋에 자동 레이블링된 자동차 3D 모델 데이터(3000개 정점)를 제공하며, PaddlePaddle 및 PyTorch 구현이 포함되어 있습니다. DLA-34 백본과 변형 가능한 합성곱(DCNv2)을 활용하여 Moderate 환경에서 14.17%의 Car 클래스 감지 성능을 달성했습니다. MIT 라이선스로 배포되며, 3D 감지 및 컴퓨터 비전 연구에 활용 가능합니다.