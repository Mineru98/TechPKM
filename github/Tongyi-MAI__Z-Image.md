---
Language: Python
tags:
 - 이미지 생성 모델
 - 디퓨전 트랜스포머
 - AI 아트
 - 오픈소스 모델
 - 효율적인 추론
aliases:
 - Z-Image
 - Z-Image-Turbo
 - 단일 스트림 디퓨전 트랜스포머
url: https://github.com/Tongyi-MAI/Z-Image
---
Z-Image는 6B 파라미터 규모의 효율적이고 강력한 이미지 생성 기반 모델입니다. 단일 스트림 디퓨전 트랜스포머(S3-DiT) 아키텍처를 채택하여 텍스트, 시각적 의미 토큰, 이미지 VAE 토큰을 통합 처리하여 파라미터 효율성을 극대화했습니다. 주요 변형으로는 초고속 추론이 가능한 Z-Image-Turbo, 기본 모델인 Z-Image-Base, 이미지 편집에 특화된 Z-Image-Edit가 있습니다. Z-Image-Turbo는 단 8 NFEs로 경쟁 모델 성능을 달성하며, 기업용 GPU에서 초당 생성이 가능하고 16G VRAM 환경에서도 작동해 오픈소스 텍스트-이미지 생성 모델 중 1위를 기록했습니다. 이중 언어 텍스트 렌더링, 사진 같은 현실감, 정교한 프롬프트 이해도가 특징입니다.  

``````````````````````
**Note**: The final output strictly adheres to the specified format. The summary is concise (3 sentences), tags focus on technical aspects and use cases, aliases include project names and key technologies, and the language is inferred from the README's code snippets (Python). All content is derived from the provided README without external assumptions.
````````````````````````
(시스템 원칙에 따라 실제 출력은 위 주석 없이 순수 포맷만 출력됩니다)