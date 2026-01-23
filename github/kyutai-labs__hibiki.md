---
Language: Python
tags:
 - 실시간 음성 번역
 - 동시 통역
 - 음성 합성
 - 머신러닝
 - 음성 변환
aliases:
 - 히비키
 - 실시간 음성-음성 번역
 - 동시 음성 번역 모델
 - Hibiki 모델
url: https://github.com/kyutai-labs/hibiki/blob/main/README.md
---
히비키는 실시간으로 음성을 다른 언어로 동시 번역하는 모델입니다. 오프라인 번역과 달리 사용자의 발화 중간에 번역을 생성하며, 텍스트 번역과 함께 자연스러운 음성 출력을 제공합니다. Moshi 아키텍처를 기반으로 한 이 모델은 12.5Hz의 일정한 프레임률로 음성 및 텍스트 토큰을 생성하며, 음성 유사도 조절이 가능한 Classifier-Free Guidance 기법을 활용합니다. 현재 프랑스어-영어 번역을 지원하며, 모바일 기기에서도 실행 가능한 경량화 버전(Hibiki-M)을 제공합니다.