---
Language: Python  
tags:  
 - Apple Silicon  
 - 머신러닝 프레임워크  
 - NumPy/PyTorch 호환  
 - 고성능 배열 연산  
 - 크로스플랫폼 지원  
aliases:  
 - MLX 프레임워크  
 - Apple ML 연구 도구  
 - Python C++ Swift 통합 ML  
url: https://github.com/ml-explore/mlx  
---  
MLX는 Apple Silicon 기반 머신러닝 연구를 위한 고성능 배열 프레임워크입니다. NumPy와 유사한 Python API를 제공하며, PyTorch 스타일의 고수준 API(mlx.nn, mlx.optimizers)로 복잡한 모델 개발을 간소화합니다. CPU/GPU 통합 메모리 모델과 지연 실행(lazy computation) 기능을 통해 효율적인 연산과 동적 그래프 구성을 지원합니다. C++, C, Swift API와의 호환성으로 다양한 언어 환경에서 활용 가능한 것이 특징입니다.  

```markdown
### 주요 특징
- **통합 메모리 모델**: 장치 간 데이터 이동 없이 CPU/GPU 연산 가능  
- **자동 미분/벡터화**: 함수 변환 기반 최적화 지원  
- **동적 그래프**: 인풋 변경에 따른 재컴파일 불필요  
- **멀티디바이스 지원**: macOS(Apple Silicon) 및 Linux(CUDA/CPU) 호환  
```