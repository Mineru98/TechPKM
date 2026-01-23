---
Language: Python
tags:
 - LLM
 - 멀티모델 비교
 - React
 - FastAPI
 - OpenRouter
aliases:
 - LLM평의회
 - llm-council
 - 다중모델 평가
url: https://github.com/karpathy/llm-council
---
이 프로젝트는 여러 LLM(대형 언어 모델)을 "평의회" 형태로 구성하여 단일 질문에 대한 다중 모델 응답을 비교·분석하는 로컬 웹 애플리케이션입니다. 사용자로부터 질문을 입력받아 OpenRouter를 통해 여러 모델에 분산 처리하고, 모델 간 상호 평가 및 순위 매기기 과정을 거쳐 최종 답변을 생성합니다. 기술 스택은 Python(FastAPI) 백엔드와 React 프론트엔드로 구성되며, JSON 파일에 대화 기록을 저장합니다. 'Vibe Code' 형태로 개발되어 지속적인 지원은 제공되지 않습니다.