---
Language: Python  
tags:  
 - 3D Reconstruction  
 - Fruit Counting  
 - Neural Radiance Fields  
 - Computer Vision  
 - Agriculture Automation  
aliases:  
 - FruitNeRF  
 - 과일 계수 프레임워크  
 - 과일 3D 계수  
 - Neural Radiance Fields 농업  
url: https://github.com/meyerls/FruitNeRF  
---  
FruitNeRF는 다양한 과일 유형을 3D 공간에서 직접 계수하기 위한 통합 프레임워크입니다. 이 시스템은 단안 카메라로 촬영한 포즈 이미지와 고급 분할 모델을 활용해 과일에 대한 이진 마스크를 생성하고, 이를 기반으로 의미론적 신경망 방사장(Semantic Neural Radiance Field)을 훈련시킵니다. 추출된 과일 전용 포인트 클라우드에 계층적 클러스터링을 적용하여 정확한 계수를 수행하며, 기존 2D 기반 방법론의 한계(예: 중복 계수, 관련 없는 과일 계수)를 극복합니다. 실제 사과나무와 합성 데이터(애플, 레몬, 망고 등)를 통해 검증되었으며, U-Net 대비 파운데이션 모델 기반 분할 성능을 비교 평가합니다.  

### 핵심 기능  
1. **3D 기반 과일 계수**: COLMAP과 Nerfstudio를 활용한 3D 재구성  
2. **범용 분할 모델**: Grounding-SAM 및 SAM-HQ 통합  
3. **확장성**: 사용자 데이터 및 공개 데이터셋(FruitNeRF, Fuji) 지원  
4. **모듈식 설계**: 볼륨 샘플링 → 포인트 클라우드 클러스터링 파이프라인  

### 기술 스택  
- Python, PyTorch, Nerfstudio, GroundingDINO, Segment Anything Model (SAM)  
- 3D 재구성: Neural Radiance Fields (NeRF)  
- 클러스터링: DBSCAN 기반 계층적 알고리즘  

### 적용 분야  
- 스마트 농업, 과수원 자동화, 농산물 품질 관리  

### 데이터셋  
- **실제 데이터**: 3개 사과나무(수동 계수 GT) + 벤치마크 사과 데이터셋  
- **합성 데이터**: 애플, 배, 레몬, 복숭아, 망고, 자두  
- Zenodo를 통해 공개 (DOI: 10.5281/zenodo.10869455)