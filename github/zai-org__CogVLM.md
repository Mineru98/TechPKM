---
Language: Python  
tags:  
 - 시각 언어 모델  
 - 멀티모달 AI  
 - GUI 에이전트  
 - 오픈소스 VLM  
 - 이미지 이해  
aliases:  
 - CogVLM  
 - CogAgent  
 - 시각적 언어 모델  
 - GUI 에이전트 모델  
 - 멀티턴 대화 모델  
url: https://github.com/THUDM/CogVLM  
---
CogVLM과 CogAgent는 이미지와 텍스트를 이해하는 오픈소스 시각 언어 모델(VLM)입니다. CogVLM-17B는 490×490 해상도의 이미지 이해 및 멀티턴 대화를 지원하며, 10개 크로스모달 벤치마크에서 SOTA 성능을 보입니다. CogAgent-18B는 CogVLM을 기반으로 1120×1120 고해상도 처리와 GUI 에이전트 기능을 추가해 웹/앱 인터페이스 작업(예: AITW, Mind2Web)에서 우수한 성능을 발휘합니다. 웹 데모와 CLI, 파인튜닝 도구를 제공하며, 4비트 양자화로 저사양 GPU에서도 실행 가능합니다.  

- **CogVLM**: 이미지 설명, 시각 QA, 그라운딩(객체 좌표 추출)  
- **CogAgent**: 고해상도 이미지 처리, GUI 작업 계획 수립, 좌표 기반 액션 생성  
- **주요 기술**: SAT/Hugging Face 지원, 4비트 양자화, OCR-Free 추론  
- **응용 분야**: 교육용 AI, 자동화 도구, 멀티모달 챗봇, 문서 분석  

> 🌟 CogVLM2(llama3-8B 기반)는 GPT-4V 수준의 성능을 제공하며, [공식 GitHub](https://github.com/THUDM/CogVLM2)에서 다운로드 가능합니다.