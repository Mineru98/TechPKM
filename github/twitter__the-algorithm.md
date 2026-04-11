---
Language: Scala
tags:
 - RecommendationSystem
 - MachineLearning
 - Scala
 - Rust
 - Python
aliases:
 - X Recommendation Algorithm
 - Twitter Recommendation Algorithm
 - 트위터 추천 알고리즘
url: https://github.com/twitter/the-algorithm/blob/main/README.md
---
X의 추천 알고리즘은 '추천 타임라인' 및 '추천 알림' 등 X 제품 전반의 피드를 구성하고 제공하는 핵심 서비스와 모델들의 집합입니다. 후보자 생성, 랭킹, 필터링 과정을 거쳐 타임라인을 구성하며, SimClusters와 TwHIN 같은 임베딩 모델과 GraphJet 기반의 그래프 처리 기술을 활용합니다. Rust 기반의 고성능 ML 모델 서빙 프레임워크인 navi와 피드 구성 프레임워크인 product-mixer 등 다양한 소프트웨어 프레임워크를 공통 기반으로 사용하여 시스템을 구축했습니다.