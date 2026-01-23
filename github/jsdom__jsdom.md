---
Language: JavaScript  
tags:  
 - DOM 구현  
 - Node.js 테스트  
 - HTML 파서  
 - 웹 스크래핑  
 - 가상 브라우저  
aliases:  
 - jsdom  
 - JavaScript DOM 구현  
 - jsdom 라이브러리  
 - Node.js 웹 테스트  
url: https://github.com/jsdom/jsdom  
---
jsdom은 WHATWG DOM 및 HTML 표준을 Node.js 환경에서 순수 JavaScript로 구현한 프로젝트입니다. 실제 웹 애플리케이션 테스트 및 스크래핑을 위해 브라우저의 핵심 기능을 에뮬레이션하는 것을 목표로 합니다. `JSDOM` 생성자를 통해 HTML 문자열을 DOM으로 변환하고, 가상 윈도우 객체를 활용해 브라우저 환경에서만 사용 가능한 API를 지원합니다. 스크립트 실행, 리소스 로딩, 가상 콘솔, 쿠키 관리 등의 기능을 제공하며, PhantomJS와 달리 시각적 렌더링 및 레이아웃 기능은 포함하지 않습니다. 웹 표준 미지원 부분에 대한 경고 및 오류 처리 메커니즘이 내장되어 있습니다.