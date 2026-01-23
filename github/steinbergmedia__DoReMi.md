---
Language: XML  
tags:  
 - OMR  
 - 데이터셋  
 - 음악 인식  
 - 딥러닝  
 - MusicXML  
aliases:  
 - DoReMi 데이터셋  
 - Dorico OMR 데이터  
 - Steinberg QMUL 협업 프로젝트  
url: https://github.com/steinbergmedia/DoReMi/blob/main/README.md  
---  
DoReMi는 OMR(광학 음악 인식) 연구를 위한 종합 데이터셋으로, Steinberg의 Dorico 팀과 QMUL의 협력으로 제작되었습니다. 이 데이터셋은 Dorico 소프트웨어를 활용해 생성된 다양한 데이터 유형(이미지, MusicXML, OMR 메타데이터, MIDI, MEI)을 포함하며, 약 6,432개의 악보 이미지와 94개 클래스의 100만 개 이상의 어노테이션 객체를 제공합니다. 클래스 불균형 문제가 존재하지만, 페이지 수, 클래스 수, 오선 수 등의 요구사항에 맞춘 사전 정의된 서브셋도 포함되어 있습니다. 데이터셋의 주요 목적은 딥러닝 기반 OMR 기술 발전과 기존 데이터셋(Muscima++, DeepScores)과의 호환성 강화에 있습니다. 공개된 버전은 저작권 문제가 없는 악보만 포함하며, 전체 데이터셋으로 학습된 모델도 제공될 예정입니다.