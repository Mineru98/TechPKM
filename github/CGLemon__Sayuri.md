---
Language: C++
tags:
 - 바둑 엔진
 - AlphaZero 알고리즘
 - MCTS
 - 딥러닝
 - GTP 프로토콜
aliases:
 - Sayuri 바둑 엔진
 - GTP 호환 Go 엔진
 - AlphaZero 스타일 바둑 AI
url: https://github.com/CGLemon/Sayuri
---
Sayuri는 Deep Convolutional Neural Networks와 Monte Carlo Tree Search(MCTS)를 기반으로 한 GTP 호환 바둑 엔진입니다. AlphaZero 스타일 알고리즘을 사용하여 인간의 전략 없이도 바둑을 학습할 수 있으며, Leela Zero와 KataGo의 연구를 기반으로 다양한 규칙, 코미 설정, 보드 크기를 지원합니다. 효율적인 자체 대국 학습 시스템을 통해 계산 비용을 크게 줄였으며, CUDA 추론 백엔드 또는 TensorRT를 활용한 최적화 버전이 존재합니다.  

이 프로젝트는 C++로 구현되었으며, Python 기반 경량 엔진도 제공합니다. Sabaki 또는 GoGui와 같은 GTP 인터페이스를 통해 사용할 수 있으며, 효율적인 자체 대국 학습 시스템으로 3개월 만에 단일 GPU로 완전한 훈련 과정을 수행할 수 있습니다.