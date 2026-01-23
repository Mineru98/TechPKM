---
Language: Python  
tags:  
 - 객체 환각 평가  
 - 대규모 비전-언어 모델  
 - 자동 세분화  
 - 자연어 처리  
 - EMNLP 2023  
aliases:  
 - POPE 평가 도구  
 - 객체 존재 여부 검증  
 - LVM 환각 감지  
 - COCO 기반 POPE  
url: https://github.com/Yifan-Li-EE/POPE  
---
이 프로젝트는 대규모 비전-언어 모델(LVLM)에서 발생하는 객체 환각 현상을 평가하기 위한 POPE(Polling-based Object Probing Evaluation) 방법론과 코드 및 데이터를 제공합니다. COCO 등의 객체 어노테이션 데이터셋 또는 SEEM과 같은 자동 세분화 도구를 활용해 기준 객체를 추출하고, 다양한 부정 샘플 전략을 적용한 평가 데이터셋을 구축할 수 있습니다. 정확도, 정밀도, 재현율, F1 점수, 긍정 응답 비율 등의 지표를 통해 모델 성능을 분석합니다. EMNLP 2023에 논문으로 게재되었습니다.