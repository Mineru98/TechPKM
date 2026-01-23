---
Language: Python/JavaScript
tags:
 - 이미지 세그멘테이션
 - 비디오 처리
 - SAM 모델
 - XMem 모델
 - 웹 기반 도구
aliases:
 - 세그드로워
 - SegDrawer
 - SAM2 세그멘테이션
 - 인터랙티브 마스크 생성기
url: https://github.com/lujiazho/SegDrawer
---
SegDrawer는 웹 기반 정적 마스크 생성 도구로, Segment Anything Model(SAM), XMem, SAM2를 활용한 시맨틱 드로잉과 비디오 세그멘테이션 전파를 지원합니다. 사용자는 이미지를 업로드해 인터랙티브하게 마스크를 그리거나, 첫 프레임 마스크를 기반으로 비디오 세그멘테이션을 수행할 수 있습니다. 웹 인터페이스는 SAM2를 기본으로 사용하며, 다양한 도구(클리어, 지우개, 다운로드 등)를 제공합니다. 로컬 실행 시 백엔드 서버 설정이 필요하며, Colab 튜토리얼도 제공됩니다.  

> 핵심 기능:  
> - SAM/XMem/SAM2 기반 세그멘테이션  
> - 인터랙티브 마스크 편집  
> - 비디오 프레임별 마스크 전파  
> - 웹 기반 실시간 처리