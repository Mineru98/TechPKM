---
Language: XML, PNG, MIDI, MEI, MusicXML, Dorico  
tags:  
 - OMR  
 - 음악 인식  
 - 데이터셋  
 - 딥러닝  
 - 음악 표기법  
aliases:  
 - DOReMi  
 - Dorico OMR 데이터셋  
 - Steinberg QMUL 협력 프로젝트  
url: https://github.com/steinbergmedia/DoReMi  
---
DOReMi는 Steinberg의 Dorico 팀과 QMUL(Elona Shatri 및 George Fazekas)의 협력으로 개발된 OMR(Optical Music Recognition) 연구용 데이터셋입니다. 이 데이터셋은 Dorico 소프트웨어에서 생성된 5가지 유형의 데이터(악보 이미지, MusicXML, OMR 메타데이터, MIDI, MEI)를 포함하며, 기존 OMR 연구의 한계를 보완하기 위해 풍부한 음악 정보를 제공합니다. 6,432개의 악보 이미지와 약 100만 개의 주석 객체를 포함하며, 94개의 클래스로 분류된 객체들이 강조된 클래스 불균형(줄기와 음표 머리가 절반 차지)을 보입니다. DeepScores의 1/50, Muscima++의 42배 규모로 구성되어 있으며, 딥러닝 기반 OMR 연구에 활용 가능합니다.  

데이터셋은 공개 가능한 악보로 구성되어 있으며, 향후 사전 학습 모델도 공개될 예정입니다. OMR 메타데이터에는 바운딩 박스, 픽셀 마스크, 음악적 속성(지속 시간, 음높이 등)이 포함되어 있어 객체 감지 및 분할 작업에 최적화되어 있습니다. 또한 Muscima++ 및 DeepScores와의 호환성을 통해 통합 실험이 가능합니다.