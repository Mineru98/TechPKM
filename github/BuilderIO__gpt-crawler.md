---
Language: TypeScript
tags:
 - 크롤러
 - GPT
 - OpenAI
 - 웹스크래핑
 - 커스텀GPT
aliases:
 - gpt-크롤러
 - 커스텀GPT생성
 - 웹사이트지식추출
url: https://github.com/BuilderIO/gpt-crawler
---
이 프로젝트는 특정 웹사이트나 여러 URL을 크롤링하여 지식 파일을 생성하고, 이를 기반으로 맞춤형 GPT를 만들 수 있도록 지원합니다. 구성 파일에서 크롤링 대상 URL과 선택자를 지정하면, 지정된 웹 페이지의 콘텐츠를 추출하여 JSON 파일로 출력합니다. 생성된 파일은 OpenAI 플랫폼에 업로드하여 커스텀 GPT나 어시스턴트를 생성하는 데 활용할 수 있습니다. Node.js 기반의 크롤러와 Docker 컨테이너, API 서버 실행 옵션을 제공합니다.