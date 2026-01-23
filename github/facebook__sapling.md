---
Language: Rust  
tags:  
 - 분산형 소스 제어 시스템  
 - Git 호환  
 - 대규모 저장소 최적화  
 - CLI 도구  
 - 오픈소스  
aliases:  
 - Sapling SCM  
 - Sapling CLI  
 - 슬링  
 - 분산형 버전 관리  
url: https://github.com/facebook/sapling  
---  
Sapling SCM은 수백만 개의 파일과 커밋을 처리할 수 있는 확장성을 가진 Git 호환 소스 제어 시스템입니다. 사용자 친화적인 인터페이스와 강력한 기능을 제공하며, EdenFS를 통해 대규모 저장소의 체크아웃 성능을 크게 향상시킵니다. Meta 내부에서 개발되었으며, CLI 도구와 웹 UI(ISL)를 포함합니다. 오픈소스 버전은 실험적 사용이 가능하지만, 일부 구성 요소(Mononoke, EdenFS)는 아직 공식적으로 지원되지 않습니다.