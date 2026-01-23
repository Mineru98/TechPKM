---
Language: Python  
tags:  
 - Spark  
 - 데이터처리  
 - RDD  
 - 데이터프레임  
 - 한국어정제  
aliases:  
 - DPS  
 - EleutherAI_DPS  
 - 데이터처리시스템  
url: https://github.com/EleutherAI/dps  
---  
# DPS (Data Processing System)  

이 프로젝트는 아파치 스파크 기반의 데이터 처리 시스템으로, RDD와 DataFrame 프레임워크를 지원합니다. JSONL 데이터를 샘플링, 중복 제거, 한국어 정제 등의 작업에 활용할 수 있으며, YAML 설정 파일로 파라미터를 관리합니다.  

## 주요 기능  
- `sample_job`: 텍스트 파일에서 JSONL 데이터 샘플링  
- `dedup_job`: MinHash를 이용한 JSONL 데이터 중복 제거  
- `korean_job`: 한국어 데이터 정제  
- 사용자 정의 작업 추가 가능  

## 사용법  
1. `python setup.py install`로 설치  
2. `python bin/sparkapp.py {job_name} --config_path=./configs/{job_name}.yaml` 명령어로 실행  

## 개발 가이드라인  
- 새로운 작업 추가 시 `dps/spark/jobs`에 Python 스크립트 작성  
- `run.py`에 작업 함수 등록 필요  
- 테스트 데이터셋 및 설정 파일 제공됨  

---