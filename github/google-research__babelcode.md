---
Language: Python
tags:
 - 코드 평가 프레임워크
 - 언어 간 호환성
 - 코드 변환
 - 실행 기반 평가
aliases:
 - BabelCode
 - 바벨코드
 - 코드 평가 도구
url: https://github.com/orlanski-gabriel/BabelCode
---
BabelCode는 다양한 언어의 데이터셋을 실행 기반으로 평가하는 프레임워크입니다. [Measuring The Impact Of Programming Language Distribution] 논문에서 제안되었으며, HumanEval, MBPP 등 다양한 데이터셋을 지원합니다. 사용자는 데이터셋을 변환하고 테스트 코드를 생성한 후 Docker 환경에서 실행 결과를 평가할 수 있습니다. 이 프레임워크는 코드 예측의 정확성과 실행 가능성을 종합적으로 검증하는 데 중점을 둡니다.