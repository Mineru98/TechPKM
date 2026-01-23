---
Language: Python  
tags:  
 - GUI grounding  
 - Visual Language Model  
 - Coordinate-free action  
 - Screen interaction  
 - Multimodal AI  
aliases:  
 - GUI-Actor  
 - 좌표 없는 GUI  
 - 화면 상호작용 모델  
 - Qwen2-VL 기반 액터  
url: https://github.com/microsoft/GUI-Actor/blob/main/README.md  
---  
GUI-Actor는 화면 좌표 생성 기반 GUI 접지의 한계를 해결하기 위한 시각-언어 모델(VLM) 기반 프레임워크입니다. 인간의 직관적인 화면 상호작용 방식을 모방하여 좌표 계산 없이도 타겟 요소를 직접 인식하고 선택할 수 있도록 설계되었습니다. Qwen2-VL/Qwen2.5-VL 백본을 활용해 ScreenSpot-Pro 및 ScreenSpot-v2 벤치마크에서 SOTA 성능을 달성했으며, 특히 7B 모델로도 72B 모델 성능을 능가하는 결과를 보여줍니다. 액션 헤드 기반의 어텐션 메커니즘과 검증 모듈을 통해 유연성과 정확도를 동시에 개선했습니다.