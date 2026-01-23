---
Language: Python  
tags:  
 - API 프록시  
 - Gemni 모델  
 - OpenAI 통합  
 - Claude Code  
 - LiteLLM  
aliases:  
 - Anthropic Proxy  
 - Claude 프록시 서버  
 - 다중 모델 프록시  
url: https://github.com/1rgs/claude-code-proxy  
---  
이 프로젝트는 Anthropic 클라이언트(예: Claude Code)를 Gemni, OpenAI 또는 직접 Anthropic 모델과 호환되도록 변환하는 프록시 서버입니다. LiteLLM을 기반으로 하여 다양한 백엔드 모델 간 원활한 요청/응답 변환을 제공하며, 환경 변수 설정을 통해 선호하는 모델 공급자와 매핑 규칙을 유연하게 구성할 수 있습니다. Claude Code와 같은 Anthropic 기반 도구를 다른 모델 환경에서 사용할 수 있도록 하는 것이 핵심 목적입니다.