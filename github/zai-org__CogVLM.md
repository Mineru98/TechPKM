---
Language: Python  
tags:  
 - 시각 언어 모델  
 - 멀티모달 AI  
 - GUI 에이전트  
 - 이미지 이해  
 - 크로스모달 벤치마킹  

aliases:  
 - CogVLM  
 - CogAgent  
 - VLM 모델  
 - GUI 에이전트 모델  
 - 시각 언어 모델 오픈소스  

url: https://github.com/zai-org/CogVLM  
---
CogVLM과 CogAgent는 오픈소스 시각 언어 모델(VLM)로, 이미지 이해와 멀티턴 대화 기능을 지원합니다. CogVLM-17B는 100억 개의 시각 파라미터와 70억 개의 언어 파라미터로 구성되어 있으며, CogAgent-18B는 1120x1120 해상도의 이미지 처리와 GUI 에이전트 기능을 추가했습니다. 두 모델은 각각 10개 및 9개의 크로스모달 벤치마크에서 최고 성능을 달성했으며, 이미지 기반 작업(예: GUI 조작, 좌표 기반 그라운딩)에 특화된 기능을 제공합니다.  

CogVLM은 이미지 설명, 시각적 질의응답, 복잡한 계산 문제 해결 등에 강점을 보이며, CogAgent는 웹/앱 인터페이스에서의 작업 계획 수립 및 좌표 기반 액션 생성이 가능합니다. SAT 및 Hugging Face를 통해 배포되며, 4비트 양자화를 지원하여 11GB GPU 메모리로 실행 가능합니다.  

### 주요 기능  
- **CogVLM**: 멀티턴 대화, 이미지 캡션링, 시각적 그라운딩  
- **CogAgent**: 고해상도 이미지 처리(1120x1120), GUI 작업 계획 수립, 좌표 기반 액션 생성  
- **벤치마크**: VQAv2, POPE, MM-VET, AITW, Mind2Web 등에서 SOTA 성능 달성  
- **배포 옵션**: CLI, 웹 데모, OpenAI Vision 포맷 API, 파인튜닝 지원  

### 기술 스택  
- 언어 모델: Vicuna-7B 기반  
- 프레임워크: SAT(SwissArmyTransformer), Hugging Face Transformers  
- 하드웨어: NVIDIA RTX 3090/4090 또는 A100 GPU 권장  

### 라이선스  
- 코드: Apache-2.0  
- 모델 가중치: 별도 모델 라이선스 준수 필요