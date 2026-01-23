---
Language: JavaScript
tags:
 - 마크다운 렌더러
 - React 컴포넌트
 - 플러그인 지원
 - 보안 우선
 - GitHub Flavored Markdown
aliases:
 - react-markdown
 - React 마크다운
 - 안전한 마크다운 렌더링
 - GFM 지원
url: https://github.com/remarkjs/react-markdown
---
이 프로젝트는 React 애플리케이션에서 마크다운을 안전하게 렌더링할 수 있는 컴포넌트를 제공합니다. `dangerouslySetInnerHTML`을 사용하지 않아 XSS 공격으로부터 보호되며, 커스텀 컴포넌트와 다양한 플러그인을 통한 확장성을 지원합니다. CommonMark 표준을 완전히 준수하며, `remark-gfm` 플러그인을 통해 GitHub Flavored Markdown(GFM)까지 완벽하게 처리할 수 있습니다. 초보자부터 고급 사용자까지 쉽게 활용할 수 있도록 설계되었으며, 비동기 플러그인 처리도 지원합니다.