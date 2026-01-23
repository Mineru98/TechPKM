---
Language: Python  
tags:  
 - 코드 평가 프레임워크  
 - 다국어 코드 실행  
 - 데이터셋 변환  
 - 실행 기반 평가  
 - 프로그래밍 언어 비교  
aliases:  
 - BabelCode  
 - 실행 기반 코드 평가기  
 - 다국어 코드 변환기  
 - BabelCode 프레임워크  
url: https://github.com/google-research/babelcode  
---
BabelCode는 다양한 언어로 작성된 데이터셋을 실행 기반으로 평가하는 프레임워크입니다. [Measuring The Impact Of Programming Language Distribution] 논문에서 제안된 이 도구는 코드 변환, 테스트 생성, 실행 평가를 자동화하여 언어별 코드 품질을 객관적으로 비교할 수 있도록 설계되었습니다. 주요 기능으로는 데이터셋 변환, 테스트 코드 생성, 언어별 실행 결과 분석 및 실패 사례 추적이 포함됩니다. Docker와 Python 기반으로 동작하며 HumanEval, MBPP 등 표준 코드 벤치마크를 지원합니다.