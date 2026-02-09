---
Language: Python
tags:
 - ComputerVision
 - SAM
 - CLIP
 - ImageSegmentation
 - Gradio
aliases:
 - Segment Anything
 - SAM with CLIP
 - 텍스트 프롬프트 기반 이미지 분할
url: https://github.com/Curt-Park/segment-anything-with-clip
---
이 프로젝트는 Meta의 SAM(Segment Anything Model)이 제공하는 모든 객체 제안을 생성하고, 각 영역에 대해 OpenAI의 CLIP을 활용해 텍스트 프롬프트와의 유사도를 계산하여 가장 적합한 객체를 분할합니다. 사용자가 자연어 텍스트를 입력하면 이미지 내에서 해당하는 객체를 자동으로 식별하고 마스크를 생성할 수 있으며, Gradio를 통해 로컬 환경에서 쉽게 실행해볼 수 있습니다. 이는 아직 공개되지 않은 SAM의 텍스트 프롬프트 기능을 CLIP과 결합하여 구현한 독창적인 접근 방식입니다.