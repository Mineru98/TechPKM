---
Language: Python  
tags:  
 - OCR  
 - 문서지능  
 - 핸드라이팅인식  
 - 테이블추출  
 - 마크다운변환  
aliases:  
 - Chandra-OCR  
 - 복잡한문서OCR  
 - 다국어문서처리  
url: https://github.com/datalab-to/chandra  
---
Chandra는 복잡한 문서(필기, 표, 수학식, 양식 등)를 처리하는 최첨단 OCR 모델입니다. 핸드라이팅, 병합 셀 처리, LaTeX 수학식 변환, 양식 필드 재구성 등 다양한 문서 유형을 지원하며, 마크다운/HTML/JSON 등 구조화된 레이아웃 메타데이터를 출력합니다. HuggingFace 또는 vLLM 서버를 통한 로컬 실행이 가능하며, 40개 이상의 언어를 지원합니다.  

**핵심 특징**:  
- 필기체 및 지저분한 인쇄체 인식  
- 병합 셀 보존 표 추출  
- 인라인/블록 수학식 LaTeX 변환  
- 체크박스/라디오 버튼 포함 양식 재구성  
- 다중 컬럼, 신문, 교과서 등 복잡한 레이아웃 처리  

**기술 스택**: Python, HuggingFace Transformers, vLLM, Docker  

**사용 사례**: 의료 기록, 재무제표, 과제 답안지, 연구 논문 등 복잡한 문서 디지털화.