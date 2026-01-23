---
Language: Go
tags:
 - ONNX 런타임
 - 딥러닝 추론
 - 크로스 플랫폼
 - Go 바인딩
 - 신경망 실행
aliases:
 - onnxruntime-go
 - 온닉스런타임 Go 래퍼
 - Go ONNX 실행기
url: https://github.com/yalue/onnxruntime_go
---
이 프로젝트는 Go 코드에서 ONNX 형식의 신경망을 로드하고 실행할 수 있는 크로스 플랫폼 래퍼 라이브러리를 제공합니다. Windows, Linux, macOS에서 작동하며 CGo를 통해 온닉스런타임 공유 라이브러리를 수동으로 로드하여 MSVC/Mingw 호환성 문제를 해결합니다. Go 제네릭을 활용해 다양한 텐서 데이터 형식을 지원하며 CUDA, TensorRT 등 가속 실행 제공자를 통합합니다. 사용자는 공유 라이브러리 경로를 설정한 후 세션 생성 및 추론을 간편하게 수행할 수 있습니다.