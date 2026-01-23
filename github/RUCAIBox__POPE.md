---
Language: Python  
tags:  
 - vision-language-models  
 - hallucination-evaluation  
 - object-detection  
 - benchmarking  
 - NLP  
aliases:  
 - POPE  
 - Object-Hallucination-Evaluation  
 - LVLM-Benchmark  
 - POPE-EMNP2023  
url: https://github.com/RUCAIBox/POPE  
---  
POPE(Polling-based Object Probing Evaluation)는 대규모 비전-언어 모델(LVLM)의 객체 환각 현상을 평가하기 위한 벤치마크입니다. COCO 등의 데이터셋에서 객체 주석을 활용하거나 SEEM과 같은 자동 분할 도구를 사용하여 평가 세트를 구성할 수 있으며, 랜덤/인기/적대적 샘플링 전략을 기반으로 한 질문 생성 방식을 제공합니다. 정확도, 정밀도, 재현율, F1 점수 등의 지표를 통해 모델의 객체 인식 성능을 종합적으로 평가할 수 있습니다.  

```python
# 설치 및 실행 예시
python main.py --auto_seg True --img_path ./segmentation/coco_val_images.json --seg_num 1000
```