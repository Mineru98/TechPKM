---
Language: Python  
tags:  
 - 텍스트 음성 변환  
 - Microsoft Edge TTS  
 - 음성 합성  
 - Python 모듈  
aliases:  
 - edge-tts  
 - edge-playback  
 - TTS 서비스  
url: https://github.com/rany2/edge-tts  
---
`edge-tts`는 Python 코드 또는 커맨드 라인에서 Microsoft Edge의 클라우드 기반 텍스트 음성 변환(TTS) 서비스를 사용할 수 있게 하는 모듈입니다. 음성 생성, 재생, 자막 생성 기능을 지원하며 다양한 언어와 음성 옵션을 제공합니다. Python 패키지 설치 또는 `pipx`를 통한 커맨드 라인 도구로 활용 가능하며, 음성 속도, 음량, 피치 조정도 지원합니다.  

### 핵심 기능  
- **다중 언어 지원**: 아랍어, 영어, 아프리칸스어 등 다양한 음성 제공  
- **음성 조정**: `--rate`, `--volume`, `--pitch` 옵션으로 음성 특성 변경 가능  
- **통합 재생**: `edge-playback`으로 즉시 음성 재생 및 자막 표시 (mpv 필요)  
- **Python 모듈**: 프로그램 내 직접 통합 가능 (예: Home Assistant, 팟캐스트 생성 툴)  

### 사용 예시  
```bash
# 기본 음성 생성
edge-tts --text "안녕하세요" --write-media hello.mp3 --write-subtitles hello.srt

# 특정 음성 사용 (예: 아랍어)
edge-tts --voice ar-EG-SalmaNeural --text "مرحبا كيف حالك؟" --write-media arabic.mp3
```  

> 📌 **참고**: SSML 사용자 정의는 Microsoft 제한으로 인해 지원되지 않음.