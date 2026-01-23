---
Language: Python
tags:
 - LLM
 - GMail
 - 이메일 분석
 - 코드 생성
 - 여행 추출
aliases:
 - GMail 여행 추출기
 - LLM 기반 이메일 분석
 - 여행지 추출 도구
url: https://github.com/run-llama/gmail-extractor
---
이 프로젝트는 LLM(Large Language Model)을 활용해 Gmail 계정 내 항공권 이메일에서 여행지를 추출하는 Python 코드입니다. 첫 번째 시도에서는 개별 이메일을 직접 분석했으나, 두 번째 접근에서는 LLM이 점진적으로 개선되는 Python 코드를 생성하도록 해 효율성을 높였습니다. 검색된 이메일에서 항공사별 패턴을 학습하며, 향후에는 스팸 필터링 강화와 로컬 모델 적용을 계획하고 있습니다.