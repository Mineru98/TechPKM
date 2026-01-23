---
Language: Python  
tags:  
 - GUI 파싱  
 - 컴퓨터 비전  
 - LLM 에이전트  
 - 스크린 분석  
 - Microsoft 연구  
aliases:  
 - OmniParser  
 - 옴니파서  
 - Pure Vision GUI Agent  
 - 스크린 파싱 도구  
 - OmniTool  
url: https://github.com/microsoft/OmniParser  
---
OmniParser는 GUI 스크린샷을 구조화된 요소로 파싱하여 LLM(예: GPT-4V)이 인터페이스 영역에 정확하게 연동된 액션을 생성할 수 있도록 지원하는 순수 비전 기반 도구입니다. Microsoft에서 개발한 이 프로젝트는 아이콘 감지, 기능 설명 예측, 상호작용 가능 여부 판단 등의 핵심 기능을 제공하며, Windows 에이전트 벤치마크에서 최고 성능을 달성했습니다. HuggingFace에 공유되는 모델은 AGPL 및 MIT 라이선스로 배포됩니다.  

```python
# 설치 방법  
conda create -n "omni" python==3.12  
pip install -r requirements.txt  
```  

주요 활용 사례로는 로컬 로그 기반 트레이닝 데이터 파이프라인 구축, 멀티 에이전트 오케스트레이션, 다양한 LLM과의 통합(OpenAI, DeepSeek, Qwen 등)이 있습니다. 최신 버전 V2는 Screen Spot Pro 벤치마크에서 39.5% 정확도를 기록하며 SOTA를 달성했습니다.