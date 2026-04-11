---
Language: TypeScript
tags:
 - React
 - Speech-to-Text
 - Web Speech API
 - Google Cloud
 - Hook
aliases:
 - react-hook-speech-to-text
 - React 음성 인식 훅
 - STT Hook
url: https://github.com/Riley-Brown/react-speech-to-text/blob/master/README.md
---
마이크 입력을 텍스트로 변환해 주는 React 커스텀 훅입니다. 기본적으로 Chrome의 SpeechRecognition API를 사용하여 별도의 설정 없이 즉시 동작하며, 옵션을 통해 Google Cloud Speech-to-Text API를 활용한 크로스 브라우저 지원도 가능합니다. 타입스크립트로 작성되었으며 외부 의존성이 없고 번들 크기가 작아 가볍게 음성 인식 기능을 프로젝트에 통합할 수 있습니다.