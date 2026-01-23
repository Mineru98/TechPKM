---
Language: Python  
tags:  
 - 소프트웨어 엔지니어링  
 - LLM 평가  
 - GitHub 이슈 해결  
 - 벤치마크 데이터셋  
 - 멀티모달 평가  
aliases:  
 - SWE-bench  
 - SWE-bench Multimodal  
 - SWE-bench Verified  
url: https://github.com/SWE-bench/SWE-bench  
---
SWE-bench는 GitHub에서 수집된 실제 소프트웨어 이슈를 기반으로 언어 모델(LM)의 코드 패치 생성 능력을 평가하는 벤치마크입니다. 제공된 코드베이스와 이슈 설명을 분석해 문제 해결 패치를 생성하는 모델의 성능을 테스트하며, Docker 기반 평가를 통해 재현성을 보장합니다. ICLR 2024 및 2025에 발표된 논문을 기반으로 하며, 멀티모달 확장 및 검증된 문제 서브셋 등을 포함합니다. Python 3.8+ 환경에서 활용 가능하며, 클라우드 기반 평가 도구(sb-cli, Modal)도 지원합니다.