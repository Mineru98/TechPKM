---
Language: Python  
tags:  
 - 트랜스포머  
 - 자연어처리  
 - 딥러닝  
 - 번역모델  
 - Pytorch  
aliases:  
 - 트랜스포머 구현  
 - transformer-ko  
 - 어텐션 모델  
 - seq2seq  
url: https://github.com/HyunwoongKo/Transformer  
---
이 프로젝트는 2017년 구글 브레인의 "Attention is All You Need" 논문을 기반으로 한 트랜스포머 모델의 자체 구현체입니다. 포지션 인코딩, 멀티 헤드 어텐션, 스케일드 닷 프로덕트 어텐션 등 트랜스포머의 핵심 구성 요소를 PyTorch를 사용하여 구현하였으며, Multi30K 데이터셋으로 독일어-영어 번역 태스크를 실험했습니다. 원본 논문과 유사한 하이퍼파라미터 설정을 사용했으며, BLEU 26.4의 점수를 기록했습니다. 단, 2019년에 작성되어 최신 모델 구현 방식과는 차이가 있을 수 있습니다.