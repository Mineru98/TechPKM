---
Language: Go
tags:
 - onnxruntime
 - 고랭
 - 크로스플랫폼
 - 머신러닝
 - 텐서
aliases:
 - onnxruntime_go
 - onnxruntime_고랭_래퍼
 - 크로스플랫폼_onnxruntime_래퍼
url: https://github.com/yalue/onnxruntime_go
---
이 프로젝트는 Go 언어에서 ONNX 형식의 신경망을 로드하고 실행할 수 있는 크로스플랫폼 `onnxruntime` 래퍼 라이브러리입니다. Windows, Linux, macOS에서 작동하며, 다양한 실행 제공자(CUDA, TensorRT 등)와 호환됩니다. Go 제네릭을 활용해 다양한 텐서 데이터 유형을 지원하며, 간단한 인터페이스로 사용이 용이합니다. Microsoft의 ONNX Runtime C/C++ API를 직접 래핑하여 MSVC 컴파일러 의존성 문제를 해결했습니다.