---
Language: Python  
tags:  
 - 멀티모달  
 - 시퀀스투시퀀스  
 - 이미지캡션  
 - VQA  
 - 텍스트생성  
aliases:  
 - OFA-Seq2Seq  
 - OFA-Multimodal  
 - Unified-Pretrained-Model  
url: https://github.com/OFA-Sys/OFA  
---  
OFA는 이미지, 텍스트, 비전-언어 작업을 통합하는 다중 모달 시퀀스투시퀀스 사전 학습 모델입니다. 영어와 중국어를 지원하며, 이미지 캡션, VQA(Visual Question Answering), 시각 근거 찾기, 텍스트-이미지 생성, 텍스트 분류 등 다양한 작업에 적용 가능합니다. 통합된 아키텍처를 통해 파인튜닝과 프롬프트 튜닝을 모두 지원하며, MMSpeech, OCR, ACL 2023 논문 등 다양한 파생 연구도 포함되어 있습니다. Hugging Face와 ModelScope를 통해 데모와 체크포인트를 제공합니다.  

OFA는 Tiny(33M)부터 Huge(930M)까지 다양한 크기의 모델을 제공하며, COCO 캡션, VQA, SNLI-VE, RefCOCO 등 벤치마크에서 경쟁력 있는 성능을 보입니다. Fairseq 및 Hugging Face Transformers와 호환되며, 텍스트-이미지 생성, 이미지 분류, GLUE 작업에도 확장 가능합니다. ICML 2022, ACL 2023에 발표된 논문을 기반으로 하며, Colab 노트북과 설치 가이드를 포함해 사용하기 쉬운 환경을 제공합니다.