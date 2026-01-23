---
Language: Python
tags:
 - 한국어-LLM
 - Large-Language-Model
 - NLP
 - 고려대학교
 - 오픈소스
aliases:
 - KULLM
 - 구름3
 - KULLM3
url: https://github.com/nlpai-lab/kullm
---
고려대학교 NLP & AI 연구실과 HIAI 연구소에서 개발한 한국어 대규모 언어 모델(KULLM) 프로젝트. KULLM3는 upstage/SOLAR-10.7B-v1.0을 기반으로 한국어 대화 및 명령어 처리에 특화된 인스트럭션 튜닝 모델입니다. 오픈소스 Apache-2.0 라이선스로 배포되며, 논문 인용 정보를 제공합니다. HuggingFace에서 모델 가중치 및 데이터셋을 공개했으며, 8×A100 GPU로 학습되었습니다.  

핵심 기능:  
- 한국어 대화 평가 최적화 (GPT-4-Turbo 기반 평가)  
- 시스템 프롬프트 기반 응답 생성 (윤리적 제약 포함)  
- 양자화(4-bit) 지원 모델 제공  
- 텍스트 스트리밍 생성 기능  

주의사항: 환각 현상 및 동어 반복 가능성 존재