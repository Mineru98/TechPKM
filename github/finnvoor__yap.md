---
Language: Swift  
tags:  
 - 음성 인식  
 - macOS CLI  
 - Speech.framework  
 - 자막 생성  
 - 오디오 트랜스크립션  
aliases:  
 - yap  
 - yap-cli  
 - macOS 음성 변환  
 - Speech.framework 트랜스크립션  
url: https://github.com/finnvoor/yap/blob/main/README.md  
---
yap은 macOS 26에서 Speech.framework를 활용해 오디오/비디오 파일의 온디바이스 음성 트랜스크립션을 수행하는 CLI 도구입니다. 텍스트 또는 SRT 형식의 출력을 지원하며, 특정 단어 검열 및 외부 도구 연동 기능을 제공합니다. 로컬에서 작동하는 빠른 음성 변환 솔루션으로, 미디어 콘텐츠 처리 및 접근성 개선에 유용합니다.  

```markdown
### 기본 사용법
- **기본 트랜스크립션**: `yap transcribe input.mp4`
- **SRT 자막 생성**: `yap transcribe input.mp4 --srt -o output.srt`
- **YouTube 영상 트랜스크립션**: `yt-dlp [URL] -x --exec yap`
```