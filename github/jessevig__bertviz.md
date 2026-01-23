---
Language: Python  
tags:  
 - Huggingface  
 - Transformer  
 - 시각화  
 - BERT  
 - Jupyter  
aliases:  
 - BertViz  
 - 트랜스포머 어텐션 시각화  
 - 어텐션 헤드 뷰  
url: https://github.com/jessevig/bertviz  
---
BertViz는 트랜스포머 언어 모델(BERT, GPT-2 등)의 어텐션 메커니즘을 시각화하는 대화형 도구입니다. Jupyter/Colab 환경에서 사용 가능하며, Huggingface 모델 대부분과 호환됩니다. 헤드 뷰, 모델 뷰, 뉴런 뷰를 통해 계층 및 헤드별 어텐션 패턴을 다각도로 분석할 수 있습니다.  

이 프로젝트는 [Tensor2Tensor 시각화 도구](https://github.com/tensorflow/tensor2tensor)를 확장하여 구현되었으며, 논문 "A Multiscale Visualization of Attention in the Transformer Model" (ACL 2019)에 기반합니다.