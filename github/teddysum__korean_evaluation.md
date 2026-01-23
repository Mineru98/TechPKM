---
Language: Python
tags:
 - 평가코드
 - 자연어처리
 - 경진대회
 - JSON-L
 - 한국어평가
aliases:
 - 국립국어원 평가코드
 - 한국어 경진대회 평가
 - Korean Evaluation Code
url: https://github.com/teddysum/korean_evaluation
---
이 프로젝트는 국립국어원 경진대회에서 사용되는 평가 코드를 제공합니다. JSON-L 형식의 정답 파일과 예측 파일을 비교하여 모델의 출력을 평가하며, 'id'와 'output' 필드를 주요 검증 대상으로 삼고 있습니다. 현재 모든 지표를 지원하지는 않으나 지속적인 확장이 예정되어 있으며, 샘플 테스트 코드와 함께 제공됩니다. 평가 과정에서는 데이터 형식 불일치 시 오류 메시지를 반환합니다.