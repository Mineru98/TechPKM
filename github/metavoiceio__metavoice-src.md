---
Language: Python
tags:
 - 음성합성
 - 오픈소스TTS
 - VoiceCloning
 - Apache2.0
 - 딥러닝
aliases:
 - MetaVoice-1B
 - 메타보이스
 - TTS모델
 - 오픈소스TTS모델
url: https://github.com/metavoiceio/metavoice-src
---
MetaVoice-1B은 100K시간 음성 데이터로 훈련된 1.2B 파라미터 규모의 오픈소스 텍스트-음성 변환(TTS) 기반 모델입니다. 영어 감정 표현, 미국식/영국식 목소리 30초 참조 오디오로 제로샷 클론링, 크로스-링구얼 보이스 클론링을 지원하며 임의 길이 텍스트 합성이 가능합니다. Apache 2.0 라이선스로 공개되어 제한 없이 사용할 수 있습니다.  

주요 특징으로는 KV-캐싱 및 배치 처리 최적화, Docker 기반 배포 지원, 파인튜닝을 통한 맞춤형 음성 생성이 포함됩니다. EnCodec 토큰 예측, 멀티밴드 디퓨전, DeepFilterNet 후처리 기술을 결합한 아키텍처를 기반으로 합니다. Python 3.10-3.11, 12GB+ VRAM GPU 환경에서 동작하며 Poetry 또는 pip를 통해 설치할 수 있습니다.