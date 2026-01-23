---
Language: Python  
tags:  
 - 유튜브 스크립트 요약  
 - langchain  
 - OpenAI-Whisper  
 - 자연어 처리  
 - 파이썬  

aliases:  
 - 유튜브 챕터 요약기  
 - YouTube Script Summarizer  
 - 영상 대본 처리 도구  
 - 챕터 기반 요약  

url: https://github.com/yourusername/youtube-script-summarizer  
---
유튜브 스크립트 요약기는 YouTube 영상의 대본을 챕터 단위로 요약하기 위한 도구입니다. yt-dlp로 영상 추출, pydub로 오디오 분할, OpenAI-Whisper로 음성 인식, langchain과 OpenAI API로 요약 기능을 구현했습니다. 정치/사회 분석 영상 등에서 챕터별 핵심 내용을 빠르게 파악하는 데 특화되어 있습니다.  

> 요약: 이 도구는 YouTube 영상의 구조화된 챕터 정보를 활용해 음성 인식 및 AI 기반 요약을 수행합니다. Python 3.11.x 환경에서 작동하며, 사용자는 영상 ID, 언어, 챕터 타임스탬프를 입력해 각 섹션별 요약본을 생성할 수 있습니다. 최종 출력은 마크다운 형식으로 제공됩니다.