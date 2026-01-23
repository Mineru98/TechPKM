---
Language: Python  
tags:  
 - 유튜브 스크립트 요약  
 - langchain  
 - OpenAI  
 - Whisper  
 - 자연어 처리  
aliases:  
 - 유튜브 강의 요약기  
 - 유튜브 챕터 요약  
 - 유튜브 스크립트 처리기  
url: https://github.com/jinhoyoo/summarize_youtube_video_lecture  
---  
Youtube Script Summarizer는 YouTube 영상 스크립트를 챕터 단위로 요약하여 핵심 내용을 추출하는 도구입니다. youtube-transcript-api, langchain, OpenAI-Whisper 등을 활용해 영상의 오디오 추출, 챕터 분할, 음성 인식, 요약 생성을 자동화합니다. 사용자는 영상 ID, 언어, 챕터 정보를 입력하면 각 섹션별 마크다운 형식의 요약본을 생성할 수 있습니다.  

핵심 기술 스택은 Python 3.11.x 기반이며, yt-dlp, pydub, OpenAI API 등의 라이브러리를 통합해 동작합니다. 영상 설명의 챕터 정보를 수동 입력해야 하는 점이 특징이며, 20분 이내의 챕터 구간에서 최적의 성능을 발휘합니다.