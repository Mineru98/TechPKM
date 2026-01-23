---
Language: Python  
tags:  
 - 키워드 추출  
 - 한국어 처리  
 - 텍스트 요약  
 - WordRank  
 - 자연어 처리  
aliases:  
 - KR-WordRank  
 - 한국어 키워드 추출기  
 - KR 키워드 분석  
url: https://github.com/lovit/kr-wordrank  
---  
KR-WordRank는 한국어 텍스트에서 비지도 방식으로 키워드와 핵심 문장을 추출하는 Python 라이브러리입니다. PageRank와 HITS 알고리즘을 기반으로 서브스트링 그래프를 구성하여 단어의 중요도를 계산하며, 키워드 벡터를 활용해 핵심 문장을 선별합니다. 영화 평 데이터 분석 등에 활용 가능하며, WordCloud 시각화와 함께 사용할 수 있습니다.  

주요 기능으로는 사용자 정의 최소 등장 빈도/최대 길이 설정, 불용어 제거, 문장 길이/유사도 기반 핵심 문장 추출이 포함됩니다. SciPy와 NumPy를 의존성으로 요구하며, Python 3.5 이상에서 동작합니다. 논문 기반의 검증된 방법론을 적용하여 한국어 텍스트 분석에 특화된 도구입니다.