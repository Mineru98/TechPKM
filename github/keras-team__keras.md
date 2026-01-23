---
Language: Python  
tags:  
 - 딥러닝 프레임워크  
 - 다중 백엔드 지원  
 - 컴퓨터 비전  
 - 자연어 처리  
aliases:  
 - Keras 3  
 - Keras  
 - 딥러닝 프레임워크  
 - Keras 백엔드 호환  
url: https://github.com/keras-team/keras/blob/master/README.md  
---  
Keras 3는 JAX, TensorFlow, PyTorch, OpenVINO(인퍼런스 전용)를 지원하는 다중 백엔드 딥러닝 프레임워크입니다. 컴퓨터 비전, 자연어 처리, 시계열 예측 등 다양한 분야에서 모델 개발과 훈련이 가능하며, 백엔드 호환성과 높은 성능을 제공합니다. 사용자는 자신의 필요에 따라 가장 빠른 백엔드를 선택하거나 기존 PyTorch/TensorFlow 코드를 재사용할 수 있습니다.  

Keras 3는 TensorFlow 백엔드 사용 시 기존 `tf.keras` 코드와 호환되며, 사용자 정의 구성요소를 최소화하면 JAX/PyTorch에서도 즉시 활용할 수 있습니다. GPU 가속 및 대규모 분산 훈련도 지원합니다.  

이 프레임워크는 "인간 친화적인" 고수준 API로 개발 속도를 높이면서도, JAX의 성능이나 TensorFlow의 생태계 같은 각 백엔드의 장점을 유연하게 활용할 수 있도록 설계되었습니다.