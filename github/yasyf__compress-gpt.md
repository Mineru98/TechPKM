---
Language: Python  
tags:  
 - 토큰 압축  
 - GPT 최적화  
 - LLM 효율성  
 - LangChain 통합  
 - 자연어 처리  
aliases:  
 - CompressGPT  
 - 프롬프트 압축기  
 - 토큰 절약 도구  
 - GPT 압축기  
url: https://github.com/yasyf/compress-gpt  
---  
CompressGPT는 GPT 프롬프트를 최대 70% 토큰 절약으로 압축하는 오픈소스 프로젝트입니다. LangChain과 통합되어 기존 프롬프트 템플릿을 교체만으로 자동 압축이 가능하며, 복잡한 설명문을 압축하여 LLM 처리 효율성을 개선합니다. 캐시 기능으로 반복 압축을 방지하며, 압축 실패 시 원본 프롬프트를 안전하게 사용합니다.  

```python
# 사용 예시
from compress_gpt.langchain import CompressPrompt as PromptTemplate
```