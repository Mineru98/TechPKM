---
Language: JavaScript
tags:
 - React
 - SpeechRecognition
 - GoogleCloudSpeechToText
 - TypeScript
 - Hook
aliases:
 - React Speech to Text
 - SpeechRecognition Hook
 - react-hook-speech-to-text
url: https://github.com/Riley-Brown/react-speech-to-text
---
이 프로젝트는 마이크로폰 입력을 텍스트로 변환하는 React 커스텀 훅입니다. 기본적으로 Chrome 브라우저에서 지원되는 Web SpeechRecognition API를 사용하며, `crossBrowser: true` 옵션을 활성화하면 Google Cloud Speech-to-Text API를 통해 크로스 브라우저 호환성을 제공합니다. 타입스크립트 기반에 0개의 의존성, 간결한 API, 4.7kB(gzipped)의 초경량 번들 크기를 특징으로 합니다. Firefox, Safari, iOS Safari 등 다양한 브라우저에서 동작하며, 실시간 음성 인식 및 중간 결과 표시 기능을 지원합니다. Google Cloud API 키 사용 시 크로스 브라우저 모드를 활성화할 수 있습니다.