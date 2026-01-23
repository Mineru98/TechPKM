---
Language: TypeScript
tags:
 - 시각화 도구
 - Claude Code
 - 그래프 분석
 - 개발자 도구
 - 오픈소스
aliases:
 - Claude Code 시각화
 - viewcc
 - 에이전트-스킬 관계 분석
url: https://github.com/kubony/claude-code-visualizer
---
View Claude Code는 Claude Code의 에이전트, 스킬, 명령어를 인터랙티브 그래프로 시각화하는 도구입니다. 프로젝트 `.claude/` 디렉토리와 글로벌 `~/.claude/` 디렉토리의 구성 요소를 자동으로 스캔하여 관계성을 분석하고, 노드 클릭 시 세부 정보를 확인하거나 UI에서 직접 실행할 수 있는 기능을 제공합니다. 로컬/글로벌 범위의 시각적 구분, 직관적인 줌/팬 컨트롤, 다양한 CLI 옵션을 지원하여 개발자 경험을 최적화했습니다.  

이 도구는 별도의 설치 없이 `npx viewcc` 명령으로 실행 가능하며, MIT 라이선스로 배포되는 오픈소스 프로젝트입니다. 주요 기술 스택은 TypeScript, React, Express로 구성되어 있습니다.