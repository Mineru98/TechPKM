---
Language: C++  
tags:  
 - AI 모델  
 - 실시간 비전 처리  
 - C++ 튜토리얼  
 - Llama C++  
 - M1 최적화  
aliases:  
 - Bakllava-Llama-CPP  
 - 실시간-바클라바-튜토리얼  
 - Apple-Silicon-LLM  
url: https://github.com/OneInterface/realtime-bakllava  
---
이 프로젝트는 C++ 기반 Llama.cpp를 활용해 Apple 실리콘 칩(M1/M2)에서 최적화된 실시간 AI 비전 처리를 구현하는 튜토리얼입니다. 웹캠 스트리밍 또는 이미지 입력을 통해 사전 훈련된 Bakllava-1 모델을 실행하는 방법을 단계별로 설명하며, macOS/Linux 환경과 Windows 호환성을 지원합니다. 주요 구성 요소로는 GUF 포맷의 양자화 모델(ggml-model-q4_k.gguf)과 토큰 매핑 파일(mmproj-model-f16.gguf)이 사용됩니다. Python 스크립트를 통해 실시간 객체 인식 및 텍스트 생성 기능을 체험할 수 있습니다.