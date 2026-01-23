---
Language: Python  
tags:  
 - OCR 도구  
 - PDF 변환  
 - Vision Language Model  
 - 문서 처리  
 - AI2 프로젝트  
aliases:  
 - olmOCR  
 - PDF-to-Markdown 변환기  
 - AllenAI OCR  
url: https://github.com/allenai/olmocr  
---
Allen Institute for AI(AI2)에서 개발한 PDF 및 이미지 기반 문서를 가독성 있는 일반 텍스트로 변환하는 오픈소스 OCR 도구. 7B 파라미터 Vision Language Model(VLM)을 기반으로 방정식과 표, 필기체, 복잡한 레이아웃을 지원하며, 헤더/푸터 자동 제거, 자연스러운 읽기 순서 유지 등의 기능을 제공. GPU 환경에서 효율적으로 동작하며, vLLM 또는 외부 서버와의 연동이 가능. Docker 지원 및 대규모 문서 클러스터링 처리 기능도 포함됨.  

**핵심 기능**  
- PDF/PNG/JPEG → 마크다운 변환  
- 방정식/표/필기체 인식  
- 멀티컬럼/복잡한 레이아웃 처리  
- AWS S3 기반 분산 처리 지원  
- Docker 컨테이너 제공  

**기술적 특징**  
- FP8 양자화 모델 적용으로 빠른 추론 속도  
- olmOCR-Bench 벤치마크(82.4점)로 성능 검증  
- vLLM 또는 원격 서버 연동 가능  
- AllenNLP 팀 개발/유지보수  

**사용 사례**  
- 학술 논문/보고서 디지털화  
- 역사적 문서 보존  
- 대량 문서 처리 파이프라인 구축  

> 설치 시 NVIDIA GPU(12GB 이상) 및 30GB 저장공간 필요. Apache 2.0 라이선스.  

---  
**참고 논문**  
1. olmOCR v1: [arXiv:2502.18443](https://arxiv.org/abs/2502.18443)  
2. olmOCR v2: [arXiv:2510.19817](https://arxiv.org/abs/2510.19817)