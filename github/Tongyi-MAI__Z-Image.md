---
Language: Python  
tags:  
 - 이미지 생성 모델  
 - 디퓨전 트랜스포머  
 - 오픈소스 AI  
 - 생성형 AI  
aliases:  
 - Z-Image  
 - Z-Image-Turbo  
 - Z-Image-Edit  
 - 단일 스트림 디퓨전 트랜스포머  
url: https://github.com/Tongyi-MAI/Z-Image  
---  
Z-Image는 **6B 파라미터**의 효율적이고 강력한 이미지 생성 기반 모델입니다. **단일 스트림 디퓨전 트랜스포머(S3-DiT)** 아키텍처를 사용하여 텍스트, 시각적 의미 토큰, 이미지 VAE 토큰을 통합 입력 스트림으로 처리합니다. 주요 변형인 **Z-Image-Turbo**는 **8 NFEs**로 초고속 추론(0.1초 미만)과 16G VRAM 호환성을 제공하며, 오픈소스 모델 중 **Artificial Analysis 리더보드 1위**를 기록했습니다. **Z-Image-Edit**는 이미지 편집 작업에 특화된 변형입니다.  

핵심 기술로는 **Decoupled-DMD**(CFG 증강과 분포 매칭 분리) 및 **DMDR**(강화 학습과 디퓨전 증류 결합) 알고리즘이 적용되어 뛰어난 성능과 안정성을 보입니다. Hugging Face, ModelScope에서 체크포인트와 온라인 데모를 제공하며, PyTorch 및 Diffusers 라이브러리에서 쉽게 활용할 수 있습니다.