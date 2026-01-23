---
Language: Python
tags:
 - State Space Model
 - 자연어 처리
 - 선형 시간 모델링
 - 딥러닝 아키텍처
 - Transformer 대체
aliases:
 - Mamba-1
 - Mamba-2
 - 선택적 상태 공간 모델
url: https://github.com/state-spaces/mamba
---
Mamba는 선택적 상태 공간 모델(Selective State Space Model) 기반의 새로운 아키텍처로, 언어 모델링과 같은 정보 밀도가 높은 데이터 처리에서 선형 시간 복잡성을 달성하면서도 Transformer 수준의 성능을 보입니다. 기존 S4 모델의 발전과 FlashAttention의 하드웨어 최적화 설계를 결합하여 구현되었으며, PyTorch 기반으로 Linux 및 NVIDIA GPU 환경에서 동작합니다. 언어 모델 외에도 다양한 시퀀스 모델링 작업에 적용 가능한 유연한 구조를 제공합니다.