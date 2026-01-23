---
Language: Python
tags:
 - 문서 이미지 파싱
 - 컴퓨터 비전
 - 멀티모달 모델
 - OCR
 - 딥러닝
aliases:
 - Dolphin
 - Dolphin-v2
 - 문서 파싱 모델
 - 바이트댄스 Dolphin
url: https://github.com/bytedance/Dolphin
---
Dolphin-v2는 디지털 및 사진 문서 모두를 처리할 수 있는 향상된 범용 문서 파싱 모델입니다. 3B 파라미터 규모로 문서 유형 인식 2단계 아키텍처와 확장 가능한 앵커 프롬프팅을 통해 레이아웃 분석, 읽기 순서 예측, 요소별 파싱을 효율적으로 수행합니다. OmniDocBench 벤치마크에서 89.78%의 종합적인 성능을 보이며, 텍스트, 표, 수식, 코드 블록 등 다양한 문서 요소를 정확하게 추출합니다. 허깅페이스와 통합되어 있으며 TensorRT-LLM 및 vLLM을 통한 가속 추론도 지원합니다.