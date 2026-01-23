---
Language: Python  
tags:  
 - Synthetic Data Generation  
 - LLM Fine-tuning  
 - Data Processing  
 - Command-line Tool  
 - Meta Llama  
aliases:  
 - Synthetic Data Kit  
 - SD Kit  
 - LLM 데이터 생성 도구  
url: https://github.com/meta-llama/synthetic-data-kit  
---  
이 프로젝트는 LLM(대형 언어 모델) 파인튜닝을 위한 고품질 합성 데이터셋을 생성하는 도구입니다. CLI 기반 4단계 프로세스(ingest → create → curate → save-as)를 통해 문서 파일 및 디렉터리에서 QA 쌍, CoT(Chain of Thought) 추론 예제 등을 생성하며, 다양한 형식으로 변환 및 저장 기능을 제공합니다. vLLM이나 외부 API와 연동해 대규모 문서 처리 및 청킹, 품질 기반 필터링 등을 지원합니다.  

주요 특징:  
- PDF/HTML/DOCX 등 다양한 포맷 지원  
- LLM을 활용한 자동 데이터 생성 및 품질 필터링  
- Alpaca/OpenAI 등 파인튜닝 호환 형식으로 변환  
- 청킹 및 배치 처리 최적화  
- YAML 설정 파일을 통한 세부 파라미터 조정 가능