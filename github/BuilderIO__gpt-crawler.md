---
Language: TypeScript
tags:
 - 웹 크롤링
 - GPT 커스텀
 - OpenAI 통합
 - 문서 분석
 - 지식 추출
aliases:
 - gpt-크롤러
 - 커스텀 GPT 생성기
 - 문서 기반 GPT 빌더
url: https://github.com/BuilderIO/gpt-crawler
---
이 프로젝트는 하나 이상의 URL에서 웹사이트를 크롤링하여 지식 파일을 생성하고 이를 기반으로 사용자 정의 GPT를 만드는 도구입니다. 크롤링을 통해 수집된 콘텐츠는 OpenAI의 커스텀 GPT 또는 어시스턴트에 업로드되어 특정 문서 기반 지식 시스템으로 활용될 수 있습니다. 사용자는 크롤링 대상 URL, 선택자, 최대 페이지 수 등의 설정을 조정하여 원하는 문서를 분석할 수 있으며, Docker 컨테이너 또는 API 서버 형태로도 실행 가능합니다.