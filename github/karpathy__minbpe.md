---
Language: Python
tags:
 - BPE
 - 토크나이저
 - 자연어처리
 - 서브워드 분할
 - 미니멀라이브러리
aliases:
 - minbpe
 - 바이트페어인코딩
 - bpe구현
url: https://github.com/karpathy/minbpe
---
이 프로젝트는 대규모 언어 모델(LLM)에서 널리 사용되는 바이트 수준의 바이트 페어 인코딩(BPE) 알고리즘을 간결하고 깨끗하게 구현한 파이썬 라이브러리입니다. GPT-2 및 GPT-4 토큰화와 호환되는 `GPT4Tokenizer`를 포함하며, 정규 표현식으로 텍스트를 전처리하는 기능을 제공합니다. `BasicTokenizer`는 더 단순한 BPE 구현체를 제공하며, 사용자는 학습 데이터를 기반으로 사용자 정의 토크나이저를 훈련시킬 수 있습니다. 특수 토큰 처리 및 토크나이저 저장/로드 기능도 포함되어 있습니다. BPE 알고리즘 연구에 적합한 교육용 코드베이스로 설계되었습니다.

## 주요 기능
- 바이트 수준 BPE 구현
- GPT-4 호환 토크나이저 제공
- 정규 표현식 기반 텍스트 전처리
- 사용자 정의 토크나이저 훈련 기능
- 특수 토큰 등록 및 처리
- 토크나이저 저장/로드 지원

## 사용 예시
```python
from minbpe import BasicTokenizer
tokenizer = BasicTokenizer()
tokenizer.train("aaabdaaabac", 256 + 3) # 256 바이트 토큰 + 3회 병합
print(tokenizer.encode("aaabdaaabac")) # [258, 100, 258, 97, 99]
```

## 확장 기능
- 대규모 파일 처리 최적화 파이썬 버전 개발 예정
- C/Rust 언어 구현 검토 중
- Llama 모델용 토크나이저 추가 검토

## 테스트
`pytest`를 사용한 테스트 케이스 제공:
```bash
$ pytest -v .
```