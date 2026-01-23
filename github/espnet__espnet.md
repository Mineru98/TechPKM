---
Language: Python
tags:
 - 음성 처리
 - 딥러닝
 - Kaldi
 - PyTorch
 - 오픈소스
aliases:
 - ESPnet 툴킷
 - ESPnet2
 - 음성 인식
 - 음성 합성
url: https://github.com/espnet/espnet
---
ESPnet은 PyTorch 기반의 통합 음성 처리 오픈소스 툴킷으로, 엔드투엔드 음성 인식(ASR), 음성 합성(TTS), 음성 번역(ST), 음성 향상(SE), 화자 분할, 음성 언어 이해(SLU) 등을 지원합니다. Kaldi 스타일의 데이터 처리와 레시피를 활용하여 다양한 실험을 위한 완전한 환경을 제공하며, 대규모 분산 학습과 모델 재현성을 위한 기능을 포함합니다. ESPnet2는 Chainer/Kaldi 의존성을 제거하고 현대적인 딥러닝 프레임워크를 기반으로 확장성을 강화했습니다. 주요 기능으로는 CTC/어텐션 하이브리드 모델, Transformer/Conformer 아키텍처, 실시간 처리, 그리고 다양한 언어/작업 지원을 포함합니다. Hugging Face와의 통합으로 모델 공유 및 추론이 가능하며, Colab/Jupyter Notebook을 통한 접근성도 제공합니다.