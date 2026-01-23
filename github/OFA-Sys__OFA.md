---
Language: Python
tags:
 - 멀티모달 모델
 - 시퀀스 투 시퀀스
 - 컴퓨터 비전
 - 자연어 처리
aliases:
 - OFA 모델
 - 통합 시퀀스 투 시퀀스 모델
 - Unified OFA
url: https://github.com/OFA-Sys/OFA
---
OFA는 영어 및 중국어를 지원하는 통합 시퀀스 투 시퀀스 사전 훈련 모델로, 시각, 언어, 크로스모달리티 작업을 통합합니다. 이미지 캡션, VQA, 시각적 근거, 텍스트-이미지 생성, 텍스트 분류 등 다양한 작업을 지원하며, 파인튜닝 및 프롬프트 튜닝을 모두 사용할 수 있습니다. MSCOCO 리더보드에서 이미지 캡션 부문에서 1위를 차지했으며, Hugging Face 및 ModelScope를 통해 데모와 체크포인트를 제공합니다. OFA는 Fairseq 및 Hugging Face Transformers와 통합되어 있으며, 다양한 작업에 대한 단계별 훈련 및 추론 절차를 제공합니다.  

OFA는 Tiny, Medium, Base, Large, Huge 버전으로 제공되며, 각각 다른 파라미터 크기와 성능을 가집니다. 이 모델은 이미지-텍스트 매칭, 이미지 인필링, 텍스트 인필링, 감지 등의 사전 훈련 작업을 지원하며, 이미지 캡션, VQA, 시각적 근거 등 다양한 다운스트림 작업에서 우수한 성능을 입증했습니다. PyTorch 및 Java 기반 COCO 평가 도구를 사용하며, 설치 및 실행을 위한 상세한 지침을 제공합니다.  

OFA는 ICML 2022에 게재되었으며, ACL 2023에서 OFA-OCR 및 OFA-프롬프트 논문이 승인되는 등 지속적으로 발전하고 있습니다. Hugging Face Spaces를 통해 온라인 데모를 제공하며, Colab 노트북을 통해 실험 절차를 쉽게 따라갈 수 있습니다.