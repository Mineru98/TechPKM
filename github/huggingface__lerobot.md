---
Language: Python  
tags:  
 - 로봇공학  
 - 머신러닝  
 - PyTorch  
 - 데이터셋  
 - 시뮬레이션  
aliases:  
 - LeRobot  
 - 허깅페이스 로봇  
 - 로보틱스 라이브러리  
url: https://github.com/huggingface/lerobot  
---
LeRobot은 PyTorch 기반의 오픈소스 로봇공학 라이브러리로, 하드웨어에 구애받지 않는 통합 인터페이스를 제공합니다. 다양한 로봇과 호환되며, 표준화된 데이터셋 형식(LeRobotDataset)과 최신 정책 모델(VLA, 강화학습 등)을 지원하여 실제 환경에 적용 가능한 솔루션을 제공합니다. Hugging Face Hub와의 통합을 통해 데이터셋 및 모델 공유가 용이하며, 교육 및 시뮬레이션 평가 기능도 포함합니다.  

핵심 기능:  
1) SO100부터 휴머노이드까지 다양한 로봇 지원  
2) Parquet + 영상 기반의 효율적인 데이터셋 관리  
3) 시뮬레이션(LIBERO, MetaWorld) 및 실제 장비 평가  
4) Imitation Learning, Reinforcement Learning, VLA 모델 구현  
5) 커스텀 하드웨어/정책 확장 가능