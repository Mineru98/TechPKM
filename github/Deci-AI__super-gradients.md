---
Language: Python  
tags:  
 - 컴퓨터비전  
 - 딥러닝  
 - SOTA모델  
 - 객체검출  
 - 포즈추정  
aliases:  
 - SuperGradients  
 - SG  
 - Deci-AI  
url: https://github.com/Deci-AI/super-gradients  
---  
SuperGradients는 프로덕션 환경에서 바로 사용 가능한 최첨단(SOTA) 컴퓨터 비전 모델을 구축, 훈련 및 미세 조정하기 위한 오픈소스 라이브러리입니다. YOLO-NAS 및 YOLO-NAS-POSE와 같은 최신 모델을 포함하여 분류, 의미 분할, 객체 검출, 포즈 추정 작업을 지원하며, 사전 훈련된 모델과 최적화된 하이퍼파라미터로 생산성을 극대화합니다. PyTorch 기반으로 TensorRT/OpenVINO와 호환되어 배포 준비가 되어 있으며, 단일 명령어로 훈련이나 추론이 가능한 사용자 친화적인 인터페이스를 제공합니다.  

---

### 요약  
SuperGradients는 다양한 컴퓨터 비전 작업을 위한 최첨단(SOTA) 모델 훈련 및 배포를 간소화하는 오픈소스 라이브러리입니다. YOLO-NAS, SegFormer 등의 모델과 사전 훈련된 체크포인트를 제공하며, 양자화 인식 훈련(QAT), 지식 증류, 분산 훈련(DDP)과 같은 고급 기능을 지원합니다. PyTorch 기반으로 TensorRT/OpenVINO와 호환되어 프로덕션 환경에 최적화되었습니다.  

### 주요 특징  
- **다양한 작업 지원**: 분류, 의미 분할, 객체 검출, 포즈 추정  
- **SOTA 모델**: YOLO-NAS, SegFormer, DEKR 등  
- **간편한 사용**: 단일 명령어로 훈련/추론 가능  
- **프로덕션 준비**: TensorRT, OpenVINO와 호환  
- **고급 기능**: 양자화, 지식 증류, 분산 훈련  

### 주요 기술 스택  
- **언어**: Python  
- **라이브러리**: PyTorch, YOLO, Albumentations  
- **배포**: ONNX, TensorRT  

### 사용 사례  
- **객체 검출**: YOLO-NAS를 활용한 실시간 검출  
- **포즈 추정**: YOLO-NAS-POSE로 정확한 포즈 인식  
- **의미 분할**: SegFormer로 고정밀 분할  
- **모델 최적화**: 양자화 인식 훈련(QAT)으로 경량화  

### 라이선스  
Apache 2.0 라이선스로 배포되어 자유롭게 사용 및 수정이 가능합니다.  

### 커뮤니티  
Slack, GitHub, Discord에서 활발한 커뮤니티가 지원됩니다.  

### 설치 방법  
```bash  
pip install super-gradients  
```  

이 프로젝트는 [DOI](https://doi.org/10.5281/zenodo.7789328)를 통해 학술적으로도 인용할 수 있습니다.